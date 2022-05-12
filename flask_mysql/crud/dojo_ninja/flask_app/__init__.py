# __init__.py
from flask import Flask


app = Flask(__name__)
app.secret_key = "dojo"

# DATABASE = "dojos_and_ninjas" #