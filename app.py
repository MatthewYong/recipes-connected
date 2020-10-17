import os
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


#Code used from https://pythonprogramming.net/decorator-wrappers-flask-tutorial-login-required/
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first!")
            return redirect(url_for('home'))
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
    return render_template("category_recipes.html", recipes=recipes, title=title)


@app.route('/add_recipe')
@login_required
def add_recipe():
    return render_template("add_recipe.html", categories=mongo.db.categories.find())


@app.route('/add_recipe_mongodb', methods=['POST'])
def add_recipe_mongodb():
    recipe = mongo.db.recipes
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('all_recipes'))


@app.route('/get_recipe/<recipe_id>')
def get_recipe(recipe_id):
    one_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("get_recipe.html", recipe=one_recipe)


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    edit_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=edit_recipe, categories=mongo.db.categories.find())


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    update_recipe = mongo.db.recipes
    update_recipe.update({"_id": ObjectId(recipe_id)},
                         {
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
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for('all_recipes'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = mongo.db.users
        user.insert_one(request.form.to_dict())
        return redirect(url_for('home'))
    return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
