from dotenv import load_dotenv
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("[·] INITIALIZATION MEBOX")
from mebox import mebox

if __name__ == "__main__":  # 👈 Esto es obligatorio para evitar errores con ProcessPoolExecutor
    load_dotenv()
    
    mebox = mebox(
        OPENROUTER_KEY = os.getenv("OPENROUTER_KEY"),
        SUPABASE_URL = os.getenv("SUPABASE_URL"),
        SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    )

    print("[·] MAKE QUERY")
    mebox.querySearch("Receta de lomo de bacalao")