from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template("index.html")  # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module 

    @app.route('/play')
    def play():
        return render_template("index.html", times = 8, row = 8, color = "red", color1 = "black")

    @app.route('/play/<int:x>')
    def play_number(x):
        return render_template("index.html", times = 8, row = x,  color = "red", color1 = "black")

    @app.route('/play/<int:x>/<int:y>')
    def play_size(x,y):
        return render_template("index.html", times = y, row = x, color = "red", color1 = "black")

    @app.route('/play/<int:x>/<int:y>/<string:color>/<string:color1>')
    def play_color(x,y,color, color1):
        return render_template("index.html", times = y, row = x, color = color, color1 = color1)
    app.run(debug=True)    # Run the app in debug mode.  # app.run(debug=True) should be the very last statement!