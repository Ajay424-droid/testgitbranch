from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Git Practice"

@app.route("/about")
def about():
    return "This is a small Flask app"

if __name__ == "__main__":
    app.run(port=5001, debug=True)

