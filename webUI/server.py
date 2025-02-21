from dotenv import load_dotenv
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.system('cls' if os.name == 'nt' else 'clear')
from mebox import mebox

from flask import Flask
from supabase import create_client, Client

# inicializar Mebox
load_dotenv()
mebox = mebox(
    OPENROUTER_KEY = os.getenv("OPENROUTER_KEY"),
    SUPABASE_URL = os.getenv("SUPABASE_URL"),
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
)

# inicializar Flask
print("\033[44m\033[01m [···] Initialize Flask \033[0m")
app = Flask(__name__)
app._static_folder = "static"
app.secret_key = '32412fb5aa7d2a0e737afe3b5325935b0a9d0a27'
app.config['MEBOX'] = mebox

app.config['supabase']: Client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

# Deshabilitar Console Logs
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Rutas
print("\033[92m",end="")
import routes
print("\033[0m",end="")