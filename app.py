from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
import models as m

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        pass
    elif request.method == "POST":
        # If search button pressed, redirect to search page
        if request.form['submit_forward'] == "search":
            return redirect(url_for('search_recipes'))
        # If add button pressed, redirect to add page
        elif request.form['submit_forward'] == "add":
            return redirect(url_for('add_recipe_index'))
        elif request.form['submit_forward'] == "home":
            recipes = m.get_all_recipes()
            return render_template('index.html', recipes=recipes)
        elif request.form['submit_forward'] == "addSubmit":
            recipe_name = str(request.form.get('name'))
            cook_time = int(request.form.get('cook_time'))
            difficulty = int(request.form.get('difficulty'))
            rating = int(request.form.get('rating'))
            m.create_recipe(recipe_name, cook_time, difficulty, rating)
        else:
            recipe = m.get_all_recipes()[0]
            return render_template('details.html', recipe=recipe)
    recipes = m.get_all_recipes()
    return render_template('index.html', recipes=recipes)



@app.route('/add', methods=["GET", "POST"])
def add_recipe_index():
    if request.method == "GET":
        pass
    elif request.method == "POST":
        if request.form['submit_forward'] == "addSubmit":
            return redirect(url_for('index'))
        elif request.form['submit_forward'] == "home":
            return redirect(url_for('index'))
    return render_template('addRecipe.html')



@app.route('/search', methods=["GET", "POST"])
def search_recipes():
    return render_template('search.html')


if __name__ == "__main__":
    app.run(debug=True)