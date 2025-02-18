from flask import request, session, render_template, redirect
from server import app

@app.route("/logout")
def logout():
    return redirect("/login", code=302)
