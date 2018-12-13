from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
import models as m

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html', recipes=m.get_all_recipes())
    elif request.method == "POST":
        print(request.form['submit_forward'])
        # If search button pressed, redirect to search page
        if request.form['submit_forward'] == "search":
            return render_template('search.html', recipes=[])
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
            m.create_recipe(recipe_name, cook_time, difficulty)

            protein = str(request.form.get('protein'))
            protein_amt = int(request.form.get('protein_amt'))
            vegetable = str(request.form.get('vegetable'))
            vegetable_amt = int(request.form.get('vegetable_amt'))
            starch = str(request.form.get('starch'))
            starch_amt = int(request.form.get('starch_amt'))
            equipment = str(request.form.get('equipment'))
            instructions = str(request.form.get('instructions'))

            if protein != 'none':
                m.create_recipe_protein(recipe_name, protein, protein_amt)
            if vegetable != 'none':
                m.create_recipe_vegetable(recipe_name, vegetable, vegetable_amt)
            if starch != 'none':
                m.create_recipe_starch(recipe_name, starch, starch_amt)
            if equipment != 'none':
                m.create_recipe_equipment(recipe_name, equipment)
            if instructions != '':
                m.create_recipe_instructions(recipe_name, instructions)
        # If we're on the search page and someone has hit the submit button
        elif request.form['submit_forward'] == "searchSubmit":
            searchName = request.form.get("searchRecipeName")
            searchDifficulty = request.form.get("searchRecipeDifficulty")
            searchRating = request.form.get("searchRecipeRating")
            searchProtein = request.form.get("searchRecipeProtein")
            searchVegetable = request.form.get("searchRecipeVegetable")
            searchStarch = request.form.get("searchRecipeStarch")
            searchVegetarian = request.form.getlist("searchRecipeVegetarian")
            searchEquipment = request.form.getlist("searchRecipeEquipment")
            print(len(searchName))
            print(searchEquipment)
            print(searchVegetarian)
            results = m.query_builder(searchName, searchRating, searchDifficulty, searchProtein, searchVegetable, searchStarch, searchVegetarian, searchEquipment)
            print(results)
            return render_template('search.html', recipes=results)
        # If we're submitting a review, 
        elif request.form['submit_forward'][:12] == "reviewSubmit":
            print("Got one")
            reviewAuthor = request.form.get('reviewAuthor')
            reviewRating = request.form.get('reviewRating')
            reviewText = request.form.get('reviewText')
            recipe_name = request.form['submit_forward'][12:]
            print(recipe_name, reviewAuthor)
            m.create_recipe_review(recipe_name, reviewAuthor, reviewRating, reviewText)
            reviews = m.get_recipe_reviews(recipe_name)
            print(reviews)
            return render_template('details.html', recipe = m.get_all_recipe_information(recipe_name), reviews = reviews)
        # Otherwise, we're trying to open or delete a recipe
        else:
            req = request.form['submit_forward']
            # Open
            if req[-4:] == "open":
                recipe_name = req[:-4]
                return render_template("details.html", recipe=m.get_all_recipe_information(recipe_name), reviews=m.get_recipe_reviews(recipe_name))
            # Delete
            else:
                m.delete_recipe(req[:-6])
                return redirect(url_for('index'))
    return render_template('index.html', recipes=m.get_all_recipes())



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



if __name__ == "__main__":
    app.run(debug=True)