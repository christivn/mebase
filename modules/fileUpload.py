from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter


def getTextFromPDF(memoryFiles, filepath):
    try:
        # Cargar el PDF
        loader = PyPDFLoader(memoryFiles.uploadsPath+filepath)
        documents = loader.load()

        # Dividir el texto en fragmentos
        splitter = CharacterTextSplitter(chunk_size=memoryFiles.chunkSize, chunk_overlap=0)
        chunks = splitter.split_documents(documents)

        return chunks

    except Exception as e:
        print(f"[X] Error processing PDF: {e}")
        return None, None
