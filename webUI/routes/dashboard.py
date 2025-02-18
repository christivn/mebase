from flask import request, session, render_template, redirect
from server import app

# Página principal (Dashboard)
@app.route("/")
def index():
    return render_template('dashboard.html')
