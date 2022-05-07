from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)    
app.secret_key = 'session'


@app.route('/')         
def dojo_home():
    return render_template("index.html") 

@app.route('/process', methods = ['POST'])
def dojo_process():
    print(request.form)
    session['full_name'] = request.form['full_name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/results')

@app.route('/results')
def dojo_results():
    full_name = session['full_name']
    location = session['location']
    language = session['language']
    comment = session['comment']
    return render_template("results.html", full_name = full_name, location = location, language = language, comment = comment)

if __name__=="__main__":    
    app.run(debug=True)   