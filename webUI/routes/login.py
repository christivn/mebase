from flask import request, session, render_template, redirect
from server import app

# Página principal (Dashboard)
@app.route("/login")
def login():
    return render_template('login.html')
