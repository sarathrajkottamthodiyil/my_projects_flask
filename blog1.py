from flask  import Flask, render_template  
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('bloghome.html')

@app.route('/enternew')
def new_member():
	return render_template('member.html')

@app.route('/memb',methods = ['POST', 'GET'])
def memb():
	if request.method == 'POST':
		try:
			nme = request.form['nme']
			top = request.form['top']
			desc = request.form['desc']








































if __name__ == '__main__':
   app.run(debug = True)