from flask import Flask, flash, redirect,render_template, request,session, abort
app = Flask(__name__)

@app.route("/")
def index():
	return "purchase!!"

@app.route("/hello/<string:name>/")
def hello(name):
    return render_template('test1.html',name=name)

if __name__ == "__main__" :
    app.run()	