from flask import request, session, render_template, redirect, jsonify
from server import app

@app.route("/register-form", methods=["POST"])
def register_form():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    try:
        response = app.config['supabase'].auth.sign_up({"email": email, "password": password})
        return jsonify({"message": "ok"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/register")
def register():
    return render_template('register.html')
