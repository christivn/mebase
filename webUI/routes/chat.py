from flask import request, session, render_template, redirect
from server import app

@app.route("/")
def chat():
    return render_template(
        'chat.html',
        aiAgent_uuid="123456789"
    )

@app.route("/<model_uuid>")
def chat_model(model_uuid):
    return render_template(
        'chat.html',
        aiAgent_uuid="123456789"
    )
