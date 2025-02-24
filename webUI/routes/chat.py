from flask import request, session, render_template, redirect
from server import app

@app.route("/")
def chat():
    return render_template(
        'chat.html'
    )

@app.route("/<model_uuid>")
def chat_model(model_uuid):
    return render_template(
        'chat.html',
        model_uuid=model_uuid
    )
