from flask import request, session, render_template, redirect
from server import app

@app.route("/agent/<agent_uuid>")
def agent(agent_uuid):
    return render_template(
        'agent.html'
    )
