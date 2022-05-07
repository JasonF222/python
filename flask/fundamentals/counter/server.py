from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)    
app.secret_key = 'session'

@app.route('/')
def counter():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    return render_template("index.html")

@app.route('/delete_session')
def clear():
    session.pop('visits')
    return redirect('/')

@app.route('/counter_session')
def add_counter():
    session['visits'] += 1
    return redirect('/')

if __name__=="__main__":  
    app.run(debug=True) 