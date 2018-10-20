from flask import Flask,render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    pname = request.form['name']
    pdojo = request.form['dojo']
    pfavLang = request.form['favLang']
    pcomment = request.form['comment']
    return render_template('result.html',name=pname, dojo=pdojo, favLang=pfavLang, comment=pcomment)

@app.route('/danger')
def danger():
    return redirect ('/')

if __name__=="__main__":
    app.run(debug=True)