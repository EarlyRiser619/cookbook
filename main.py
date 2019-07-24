from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://cook_book:coding@localhost:3306/cook_book'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'nvio)(hYFRoldsij__1@'

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120))
    source = db.Column(db.String(540))
    servings = db.Column(db.Integer)
    prep_time = db.Column(db.String(120))
    ingredients = db.Column(db.String(1000))
    instructions = db.Column(db.String(2000))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, source, servings, prep_time, ingredients, instructions, owner):
        self.title = title
        self.source = source
        self.servings = servings
        self.prep_time = prep_time
        self.ingredients = ingredients
        self.instructions = instructions
        self.owner = owner_id

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    password = db.Column(db.String(120))
    recipes = db.relationship('Recipe', backref='owner')

    def __init__(self, username, password):
        self.username = username
        self.password = password


#@app.before_request
#def require_login():
    #allowed routes
    #redirect to login page


#@app.route("/")
#def index():
    #lists titles of recipes alphabetically with authors name
    #allows for user to search for a particular recipe by title, author, ingredient, prep time


#@app.route("/newrecipe")
#def new_recipe():
    #displays form to create new recipe entry


#@app.route("/recipe")
#def find_recipe():
    #display selected recipe
    #display recipe(s) by search params


#@app.route("/register")
#def register():
    #create account


#@app.route("/login")
#def login():
    #login to user account


#@app.route("/logout")
#def logout():
    #logout of user session