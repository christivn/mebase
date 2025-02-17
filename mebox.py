import os
from tqdm import tqdm
from supabase import create_client, Client

from modules.fileUpload import getTextFromPDF
from modules.embbeding import text_to_embedding
from modules.optimization import promptOptimization

class mebox:
    def __init__(self, SUPABASE_URL, SUPABASE_KEY):
        # Supabase conection
        self.SUPABASE_URL = SUPABASE_URL
        self.SUPABASE_KEY = SUPABASE_KEY

        # Test conection
        if self.check_supabase_connection():
            supabase: Client = create_client(self.SUPABASE_URL, self.SUPABASE_KEY)

            # Uploads
            self.allowedFormats = [
                ["txt", "md", "xml", "yaml", "ini", "log", "bat", "py", "js", "java", "cpp", "html"],
                ["pdf"],
                ["json", "csv", "xlsx"]
            ]
            self.uploadsPath = "uploads/"

            # Chunking & Embedding
            self.chunkSize = 512 #Tokens
            self.chunkNeighbors = 1 #Number of chunks above and below, to improve the context
            self.embeddingModel = "thenlper/gte-small"
            self.maxChunksInContext = 20

            # Output
            self.prettify = False
        else:
            print("[X] Supabase connection error")


    def check_supabase_connection(self):
        try:
            supabase: Client = create_client(self.SUPABASE_URL, self.SUPABASE_KEY)
            response = supabase.auth.get_user()
            return True is not None
        except Exception as e:
            return False


    def fileUpload(self, filepath):
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

        if(len(chunks) > 0):
            # Generate chunks embeddings
            print("\033[34m[ GENERATING CHUNK EMBEDDINGS... ]\033[0m")
            chunkEmbeddings = []
            for chunk in tqdm(chunks, desc="Embedding chunks"):
                embedding = text_to_embedding(self, chunk.page_content)
                chunkEmbeddings.append(embedding)
                
        else:
            print("[X] Empty file, no chunks found")


    def promptOptimization(self):
        # Divide el prompt de entrada en diferentes prompts si se necesita acceder a diferentes chunks para una consulta
        return 0