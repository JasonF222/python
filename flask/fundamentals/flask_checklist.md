# Prerequisites
```
pip install pipenv
```


# Checklist
- create a new assignment folder
- navigae `into` the assignment folder
- create our virtual env
    ```
    pipenv install flask
    ```
- **WARNING** `look for pipfile.lock and pipfile`

if you don't have these files in your folder, you have an `ISSUE` which needs to get fixed `ASAP!`
- go into virtual env
    ```
    pipenv shell
    ```
- folder structure
    - pipfile
    - pipfile.lock
    - server.py

-server.py file
```py
    from flask import Flask, render_template  # Import Flask to allow us to create our app
    app = Flask(__name__)    # Create a new instance of the Flask class called "app"


    
    @app.route('/')          # The "@" decorator associates this route with the function immediately following
    def hello_world():
        return render_template("index.html")  # Return the string 'Hello World!' as a response


    # THIS NEEDS TO STAY AT THE BOTTOM
    if __name__=="__main__":   # Ensure this file is being run directly and not from a different module 
        app.run(debug=True)    # Run the app in debug mode.  # app.run(debug=True) should be the very last statement!
```