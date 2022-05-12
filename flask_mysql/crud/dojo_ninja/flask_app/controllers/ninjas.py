from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja

# Decided to put ninja approutes in dojos.py for this project #