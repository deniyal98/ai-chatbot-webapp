from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_response(user):
    user = user.lower()

    if "hello" in user:
        return "Hi! How can I help you?"
    elif "job" in user:
        return "I can help you prepare for interviews."
    elif "python" in user:
        return "Python is great for development and automation!"
    elif "bye" in user:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    response = get_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
