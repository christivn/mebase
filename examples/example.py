import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from oFiles import oFiles

if __name__ == "__main__":  # 👈 Esto es obligatorio para evitar errores con ProcessPoolExecutor
    oFiles = oFiles(
        SUPABASE_URL = "https://vzggqyxkzelgzakuxfad.supabase.co",
        SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZ6Z2dxeXhremVsZ3pha3V4ZmFkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzk0Nzk0NzAsImV4cCI6MjA1NTA1NTQ3MH0._KbsriZYe8D1acqNI1HLTuLJdQ8KdsL6sOvjVi_HEZ0"
    )

    oFiles.fileUpload("200-recetas-ultrarrapidas.pdf")