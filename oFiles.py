from modules.fileUpload import fileUpload
from modules.embbeding import text_to_embedding

class oFiles:
    def __init__(self, SUPABASE_URL, SUPABASE_KEY):
        # Supabase conection
        self.SUPABASE_URL = SUPABASE_URL
        self.SUPABASE_KEY = SUPABASE_KEY

        # Test conection

        # File
        self.complete_filename = ""
        self.filename = ""
        self.ext = ""

        # Chunking & Embedding
        self.chunkSize = 800 #tokens
        self.chunkOverlap = 300 #tokens
        self.embeddingModel = "thenlper/gte-small"
        self.maxChunksInContext = 20

    def testConnection():
        # self.SUPABASE_URL
        # self.SUPABASE_KEY
        return 0

    def fileUpload(self, filepath):
        return 0

    def embedding(self, text):
        return text_to_embedding(self, text)