import os
from supabase import create_client, Client

from modules.fileUpload import getTextFromPDF
from modules.embbeding import text_to_embedding
from modules.optimization import promptOptimization

from transformers import AutoTokenizer, AutoModel
import torch

from openai import OpenAI

class mebox:
    def __init__(self, OPENROUTER_KEY, SUPABASE_URL, SUPABASE_KEY):

        # Openrouter conection
        self.aiClient = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=OPENROUTER_KEY,
        )

        # Supabase conection
        self.SUPABASE_URL = SUPABASE_URL
        self.SUPABASE_KEY = SUPABASE_KEY

        # Test conection
        if self.check_supabase_connection():
            self.supabase: Client = create_client(self.SUPABASE_URL, self.SUPABASE_KEY)

            # Uploads
            self.allowedFormats = [
                ["txt", "md", "xml", "yaml", "ini", "log", "bat", "py", "js", "java", "cpp", "html"],
                ["pdf"],
                ["json", "csv", "xlsx"]
            ]
            self.uploadsPath = "uploads/"

            # Chunking & Embedding
            self.localEmbeddingModel = "thenlper/gte-small"
            self.chunkSize = 512 #Tokens
            self.knn = 2
            self.threshold = 0.1
            self.NeighboringChunksPairs = 1 #Number of chunks above and below, to improve the context
            self.maxChunksInContext = 20

            # CSV & XLSX
            self.csv_xlsx_knn = 20
            self.csv_xlsx_NeighboringChunksPairs = 0

            # AI Models
            self.simpleModel = "meta-llama/llama-3.1-8b-instruct"
            self.basicModel = "meta-llama/llama-3.1-70b-instruct"
            self.reasonerModel = "deepseek/deepseek-r1"

            # Output
            self.prettifyMD = False

            #-----------------------------------------------

            self.embeddingTokenizer = AutoTokenizer.from_pretrained(self.localEmbeddingModel)
            self.embeddingModel = AutoModel.from_pretrained(self.localEmbeddingModel)
        else:
            print("[X] Supabase connection error")


    def check_supabase_connection(self):
        try:
            supabase: Client = create_client(self.SUPABASE_URL, self.SUPABASE_KEY)
            response = supabase.auth.get_user()
            return True is not None
        except Exception as e:
            return False

    
    def fileToText(self, filepath):
        # Check file extension
        _, extension = os.path.splitext(filepath)
        extension = extension.lstrip('.')

        # Coming soon...
        # Text files
        # if extension in self.allowedFormats[0]:
        #     chunks = getTextFromTXT(self, filepath)

        # PDF files
        if extension in self.allowedFormats[1]:
            chunks = getTextFromPDF(self, filepath)

        # Coming soon...
        # CSV files
        # if extension in self.allowedFormats[2]:
        #     chunks = getTextFromCSV(self, filepath)

        # Coming soon...
        # Microsoft Office files
        # if extension in self.allowedFormats[2]:
        #     chunks = getTextFromMicrosoftOffice(self, filepath)

        return chunks


    def fileUpload(self, filepath):
        chunks = fileToText(filepath)
        if(len(chunks) > 0):
            # Generate chunks embeddings
            chunkEmbeddings = []
            for chunk in chunks:
                embedding = text_to_embedding(self, chunk.page_content)
                chunkEmbeddings.append(embedding)
            
            # Upload to Supabase
            self.supabase.table("files").insert({"filename": filepath}).execute()
            response = self.supabase.table("files").select("*").eq("filename", filepath).execute()
            if response.data:
                # Get file UUID
                file_uuid = response.data[0]["file_uuid"]

                f_iter = 0
                for embedding in chunkEmbeddings:
                    data = {
                        "file_uuid": response.data[0]["file_uuid"],
                        "index": f_iter,
                        "content": chunks[f_iter].page_content,
                        "embedding": embedding.squeeze().tolist()
                    }
                    self.supabase.table("chunks").insert(data).execute()
                    f_iter += 1
        else:
            print("[X] Empty file, no chunks found")


    def promptOptimization(self):
        # Divide el prompt de entrada en diferentes prompts si se necesita acceder a diferentes chunks para una consulta
        return 0


    def searchVectorsAndNeighbors(self, query):
        queryEmbedding = text_to_embedding(self, query)

        # Get cosine simility chunks
        response = self.supabase.rpc('match_chunks', {
            'query_embedding': queryEmbedding.squeeze().tolist(),
            'match_threshold': self.threshold,
            'match_count': self.knn
        }).execute()

        # Parsing the response
        results = []
        for data in response.data:
            results.append([
                data["file_uuid"],
                data["index"],
                data["content"]
            ])
        
        # Complete results with NeighboringChunksPairs
        if(self.NeighboringChunksPairs != 0):
            completeResults = []
            for x in results:
                file_uuid = x[0]
                index = x[1]

                up_neighbor = index - self.NeighboringChunksPairs
                if up_neighbor<0: up_neighbor = 0
                down_neighbor = index + self.NeighboringChunksPairs

                query = self.supabase.table("chunks").select("file_uuid, index, content") \
                .filter("file_uuid", "eq", file_uuid) \
                .filter("index", "gte", up_neighbor) \
                .filter("index", "lte", down_neighbor) \
                .execute()

                completeResults.append(query.data)
            return completeResults
        else:
            return results

    
    def promptTemplate(self, query, results):
        windowContentPrompt = "Use this information to think about your answer:"
        print(results)
        return 0

    
    def querySearch(self, query):
        results = self.searchVectorsAndNeighbors(query)
        prompt = promptTemplate(query, results)

        #completion = self.aiClient.chat.completions.create(
        #    extra_headers={
        #        "X-Title": "Mebox",
        #    },
        #    model=self.basicModel,
        #    messages=[
        #        {
        #        "role": "user",
        #        "content": query
        #        }
        #    ]
        #)
        #print(completion.choices[0].message.content)
        return 0