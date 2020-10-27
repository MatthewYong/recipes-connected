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


# Code used from https://pythonprogramming.net/decorator-wrappers-flask-tutorial-login-required/
def login_required(f):
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
    cat = {"recipe_category": category}
    recipes = mongo.db.recipes.find(cat)
    title = mongo.db.recipes.find_one(cat)
    return render_template(
        "category_recipes.html", recipes=recipes, title=title)


@app.route('/user_recipes/<user>')
@login_required
def user_recipes(user):
    user = session['user']
    logged_user = {"recipe_username": user}
    recipes = mongo.db.recipes.find(logged_user)
    return render_template("user_recipes.html", my_recipes=recipes)


@app.route('/add_recipe')
@login_required
def add_recipe():
    return render_template(
        "add_recipe.html",
        categories=mongo.db.categories.find(),
        preptime=mongo.db.preptime.find())


@app.route('/add_recipe_mongodb', methods=['POST'])
@login_required
def add_recipe_mongodb():
    recipe = mongo.db.recipes
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('all_recipes'))


@app.route('/get_recipe/<recipe_id>')
def get_recipe(recipe_id):
    one_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("get_recipe.html", recipe=one_recipe)


@app.route('/edit_recipe/<recipe_id>')
@login_required
def edit_recipe(recipe_id):
    edit_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        "edit_recipe.html",
        recipe=edit_recipe, categories=mongo.db.categories.find(),
        preptime=mongo.db.preptime.find())


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
@login_required
def update_recipe(recipe_id):
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
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for('all_recipes'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user' in session:
        return redirect(url_for('home'))
    else:
        if request.method == 'POST':
            user = mongo.db.users
            existing_user = user.find_one({
                "username": request.form['username'].lower()})
            existing_email = user.find_one({
                "email": request.form['email'].lower()})
            if existing_email is None:
                if existing_user is None:
                    # Code used from http://zetcode.com/python/bcrypt/
                    hashpass = bcrypt.hashpw(
                        request.form['password'].encode('utf-8'),
                        bcrypt.gensalt())
                    user.insert_one({
                        "email": request.form['email'].lower(),
                        "username": request.form['username'].lower(),
                        "password": hashpass})
                    session['user'] = request.form['username']
                    return redirect(url_for('home'))
                return 'The username already exist'
            return 'The emailaddress already exist'
        return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('home'))

    else:
        if request.method == 'POST':
            user = mongo.db.users
            # Code used from https://github.com/PrettyPrinted/mongodb-user-login
            login_user = user.find_one({
                "username": request.form['username'].lower()})
            # Check if user exist in database
            if login_user:
                login_pass = login_user['password']
                hashpass = bcrypt.hashpw(
                    request.form['password'].encode('utf-8'), login_pass)
                if login_pass == hashpass:
                    session['user'] = request.form['username']
                    return redirect(url_for('home'))
                return 'Invalid username/password'
            return 'Invalid username/password'
        return render_template("login.html")


# Session logout
@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop("user", None)
        flash("Logout Succesfull!")
    else:
        flash("You Are Already Logged Out")
    return redirect(url_for('login'))


# 404 Error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# 404 Error page
@app.errorhandler(500)
def internal_service_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
