from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)

@app.route('/admin')    
def hello_admin():
    return 'Hello admin'

@app.route('/success/<name>')
def success(name):
    print name
    return render_template('success.html',name=name)

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method=='POST':
        name=request.form['name']
        return redirect(url_for('success',name=name))
    else:
        return render_template('log.html')    

if __name__ == '__main__':
    app.run(debug = True)   
