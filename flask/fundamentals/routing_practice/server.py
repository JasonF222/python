from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module  
    
    @app.route('/dojo')
    def dojo():
        return 'Dojo!'
        
    @app.route('/say/<name>')
    def say(name):
        print(name)
        return "Hi " + name + "!"

    @app.route('/repeat/<number>/<statement>')
    def repeat(number, statement):
        print(number)
        print(statement)
        output = ""
        for i in range(0, int(number)):
            output += f"<h1><strong>{statement}</strong></h1>"
        return output

    @app.errorhandler(404)
    def nopass(e):
        return f"<h1><em>WHAT ARE YEW DOIN' IN MY SWAMP!??!</em></h1>"

    app.run(debug=True)    # Run the app in debug mode.  # app.run(debug=True) should be the very last statement! 