from flask import request, session, render_template, redirect
from server import app

@app.route("/")
def index():
    return render_template(
        'chat.html',
        aiAgent_uuid="123456789"
    )

@app.route("/agent/<agent_uuid>")
def agent(agent_uuid):
    return render_template(
        'agent.html'
    )
