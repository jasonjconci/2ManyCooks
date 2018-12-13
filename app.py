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

            protein = str(request.form.get('protein'))
            vegetable = str(request.form.get('vegetable'))
            starch = str(request.form.get('starch'))
            equipment = str(request.form.get('equipment'))
            instructions = str(request.form.get('instructions'))

            if protein != 'none':
                m.create_recipe_protein(recipe_name, protein)
            if vegetable != 'none':
                m.create_recipe_vegetable(recipe_name, vegetable)
            if starch != 'none':
                m.create_recipe_starch(recipe_name, starch)
            if equipment != 'none':
                m.create_recipe_equipment(recipe_name, equipment)
            if instructions != '':
                m.create_recipe_instructions(recipe_name, instructions)


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