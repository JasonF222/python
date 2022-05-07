from unicodedata import name
from flask import Flask, render_template, json  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def obj_dict(obj):
    return obj.__dict__

temp = []

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template("index.html")  # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    
    @app.route('/play')
    def play():
        return render_template("index.html", times = 3, color = "lightblue")
    
    @app.route('/play/<int:number>')
    def play_number(number):
        return render_template("index.html", times = number, color = "lightblue")

    @app.route('/play/<int:number>/<color>')
    def play_color(number, color):
        return render_template("index.html", times = number, color = color)

    @app.route('/data')
    def get_data():
        global temp
        return (json.dumps(temp, default = obj_dict))

    @app.route('/fake/<string:name>/<int:age>')
    def fake_data(name, age):
        global temp
        newperson = Person(name = name, age = age)
        temp.append(newperson)
        return (json.dumps(newperson.__dict__))

    app.run(debug=True)    # Run the app in debug mode.  # app.run(debug=True) should be the very last statement!