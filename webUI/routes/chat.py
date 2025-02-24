from flask import request, session, render_template, redirect
from server import app

@app.route("/")
def chat():
    return render_template(
        'chat.html'
    )

@app.route("/<model>")
def chat_model(model):
    return render_template(
        'chat.html'
    )
