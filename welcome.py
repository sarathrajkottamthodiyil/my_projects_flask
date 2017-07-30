from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return"welcome!!"

@app.route("/dear")
def dear():
    return "Dear Friend!"

@app.route("/morning")
def morning():
    return "good morning"

if __name__ == "__main__":
    app.run()
