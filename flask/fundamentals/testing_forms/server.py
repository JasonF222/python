from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"



@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html")  # Return the string 'Hello World!' as a response

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module 
    app.run(debug=True)    # Run the app in debug mode.  # app.run(debug=True) should be the very last statement!