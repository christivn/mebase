from flask import request, session, render_template, redirect, jsonify
from server import app

@app.route("/")
def chat():
    return render_template(
        'chat.html',
        modelDisplayName = "MeboxAI"
    )


@app.route("/chat/create", methods = ['POST'])
def create_chat():
    if request.method == 'POST':
        return jsonify({"message": "ok"}), 200


@app.route("/<model>")
def chat_model(model):
    return render_template(
        'chat.html',
        modelDisplayName = "???"
    )
