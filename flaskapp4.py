from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
	dict = {'phy':50,'che':60,'mat':70,'bio':88,'eng':79}
	return render_template('result.html', result = dict)

if __name__ == '__main__':
	app.run(debug = True)	