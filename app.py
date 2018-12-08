from flask import Flask, render_template, request
from flask_cors import CORS
import models as m

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        pass
    elif request.method == "POST":
        recipe_name = str(request.form.get('name'))
        cook_time = int(request.form.get('cook_time'))
        difficulty = int(request.form.get('difficulty'))
        rating = int(request.form.get('rating'))
        m.create_recipe(recipe_name, cook_time, difficulty, rating)

    recipes = m.get_all_recipes()
    return render_template('index.html', recipes=m.get_recipe_with_id(4))
    
if __name__ == "__main__":
    app.run(debug=True)