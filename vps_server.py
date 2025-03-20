from flask import Flask

app = Flask(__name__)

@app.route("/status")
def status():
    return "Server OK", 200


@app.route("/")
def home():
    return "Aplicatia ruleaza corect!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
