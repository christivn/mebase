from dotenv import load_dotenv
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mebox import mebox

if __name__ == "__main__":  # 👈 Esto es obligatorio para evitar errores con ProcessPoolExecutor
    load_dotenv()

    mebox = mebox(
        SUPABASE_URL = os.getenv("SUPABASE_URL"),
        SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    )

    mebox.fileUpload("200-recetas-ultrarrapidas.pdf")