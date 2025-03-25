import flask


# TODO: change this to your academic email
AUTHOR = "jeslyng@wharton.upenn.edu"


app = flask.Flask(__name__)


# This is a simple route to test your server


@app.route("/")
def hello():
    return f"Hello from my Password Validator! &mdash; <tt>{AUTHOR}</tt>"


# This is a sample "password validator" endpoint
# It is not yet implemented, and will return HTTP 501 in all situations


@app.route("/v1/checkPassword", methods=["POST"]) # policy 8 
def check_password():
    data = request.get_json()
    password = data.get("password", "")

    if len(password) < 8:
        return jsonify({"valid": False, "reason": "Password must be at least 8 characters long"}), 200

    if not re.search(r"[A-Z]", password):
        return jsonify({"valid": False, "reason": "Password must include at least one uppercase letter"}), 200

    if not re.search(r"\d", password):
        return jsonify({"valid": False, "reason": "Password must include at least one digit"}), 200

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return jsonify({"valid": False, "reason": "Password must include at least one special character"}), 200

    return jsonify({"valid": True, "reason": ""}), 200
