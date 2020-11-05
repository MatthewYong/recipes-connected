# -----------------------------------------------------------
# Flask Project for Code Institute
# Using MongoDB as database
#
# (C) 2020 Matthew Yong
# email kfm.yong@gmail.com
# -----------------------------------------------------------

import os
import bcrypt
from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from functools import wraps


from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


def login_required(f):
    """
    A decorator used for redirecting to login page when the user is not logged in. Code used from https://pythonprogramming.net/decorator-wrappers-flask-tutorial-login-required/
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)
        else:
            flash("Please Login First!")
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/all_recipes')
def all_recipes():
    return render_template("all_recipes.html", recipes=mongo.db.recipes.find())


@app.route('/category_recipes/<category>')
def category_recipes(category):
    """
    Place all recipes with the same category in one page
    """
    cat = {"recipe_category": category}
    recipes = mongo.db.recipes.find(cat)
    title = mongo.db.recipes.find_one(cat)
    # If a category does not exist in database then return to 404 error page
    if recipes.count():
        return render_template(
            "category_recipes.html", recipes=recipes, title=title)
    else:
        return render_template("404.html")


@app.route('/user_recipes/<user>')
@login_required
def user_recipes(user):
    """
    Place all useer added recipes in one page
    """
    user = session['user']
    logged_user = {"recipe_username": user}
    recipes = mongo.db.recipes.find(logged_user)
    return render_template("user_recipes.html", my_recipes=recipes)


@app.route('/add_recipe')
@login_required
def add_recipe():
    """"
    Function that finds the collections categories and preptime from MongoDB
    """
    return render_template(
        "add_recipe.html",
        categories=mongo.db.categories.find(),
        preptime=mongo.db.preptime.find())


@app.route('/add_recipe_mongodb', methods=['POST'])
@login_required
def add_recipe_mongodb():
    """"
    Function that inserts recipes into MongoDB
    """
    recipe = mongo.db.recipes
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('all_recipes'))


@app.route('/get_recipe/<recipe_id>')
def get_recipe(recipe_id):
    """"
    Function that finds a specific recipe from MongoDB
    """    
    one_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("get_recipe.html", recipe=one_recipe)


@app.route('/edit_recipe/<recipe_id>')
@login_required
def edit_recipe(recipe_id):
    """
    Edit recipe by pulling information from MongoDB and returning into edit form
    """
    edit_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "edit_recipe.html",
        recipe=edit_recipe, categories=mongo.db.categories.find(),
        preptime=mongo.db.preptime.find())


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
@login_required
def update_recipe(recipe_id):
    """
    Update the recipe that user has edited by inserting values to MongoDB.
    Code inspired from Code Institute Mini Flask Project
    """
    update_recipe = mongo.db.recipes
    update_recipe.update({"_id": ObjectId(recipe_id)}, {
        "recipe_username": request.form.get('recipe_username'),
        "recipe_name": request.form.get('recipe_name'),
        "recipe_image": request.form.get('recipe_image'),
        "recipe_category": request.form.get('recipe_category'),
        "recipe_description": request.form.get('recipe_description'),
        "recipe_preptime": request.form.get('recipe_preptime'),
        "recipe_ingredients": request.form.get('recipe_ingredients'),
        "recipe_instructions": request.form.get('recipe_instructions')
    })
    return redirect(url_for('get_recipe', recipe_id=recipe_id))


@app.route('/delete_recipe/<recipe_id>')
@login_required
def delete_recipe(recipe_id):
    """
    Delete a recipe by removing id from MongoDB. Code inspired from MongoDB documentation: https://docs.mongodb.com/manual/reference/method/db.collection.remove/
    """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for('all_recipes'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Registration of a profile by inserting information in MongoDB. If user is in session redirects to home page
    """
    if 'user' in session:
        return redirect(url_for('home'))
    else:
        # If user is not in session find username or email in a MongoDB
        if request.method == 'POST':
            user = mongo.db.users
            existing_user = user.find_one({
                "username": request.form['username'].lower()})
            existing_email = user.find_one({
                "email": request.form['email'].lower()})
            if existing_email is None:
                if existing_user is None:
                    # If username and email does not exist,
                    # hash password for extra protection.
                    # Code used from http://zetcode.com/python/bcrypt/
                    crypt_pass = bcrypt.hashpw(
                        request.form['password'].encode('utf-8'),
                        bcrypt.gensalt())
                    user.insert_one({
                        "email": request.form['email'].lower(),
                        "username": request.form['username'].lower(),
                        "password": crypt_pass})
                    session['user'] = request.form['username']
                    return redirect(url_for('home'))
                else:
                    flash('The username already exist')
                    return redirect(url_for('register'))
            else:
                flash('The email address already exist')
                return redirect(url_for('register'))
        return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login user to his/her profile
    """
    if 'user' in session:
        return redirect(url_for('home'))
    else:
        # Condition checks if user exist in database
        # Code used from https://www.youtube.com/watch?v=vVx1737auSE
        if request.method == 'POST':
            user = mongo.db.users
            logged_in = user.find_one({
                "username": request.form['username'].lower()})
            if logged_in:
                login_pass = logged_in['password']
                crypt_pass = bcrypt.hashpw(
                    request.form['password'].encode('utf-8'), login_pass)
                if login_pass == crypt_pass:
                    session['user'] = request.form['username']
                    return redirect(url_for('home'))
                else:
                    # Added text to alert user logged in has failed
                    flash("Invalid username/password")
                    return redirect(url_for('login'))
            else:
                # Added text to alert user logged in has failed
                flash("Invalid username/password")
                return redirect(url_for('login'))
        return render_template("login.html")


@app.route('/logout')
def logout():
    """
    Log out user from session using 'pop'
    """
    if 'user' in session:
        # Log out user from session
        # Code learned from https://pythonise.com/series/learning-flask/flask-session-object
        session.pop("user", None)
        flash("Logout Succesful!")
    else:
        flash("You Are Already Logged Out")
    return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(e):
    """"
    Flask error apphandler returns 404 Error page
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_service_error(e):
    """"
    Flask error apphandler returns 500 Error page
    """
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
