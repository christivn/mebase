import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from oFiles import oFiles

oFiles = oFiles(
    SUPABASE_URL = "",
    SUPABASE_KEY = ""
)

embedding = oFiles.embedding("Texto de prueba")

print(embedding)