import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def create_recipe(name, cook_time, difficulty, rating):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("insert into recipe (name, cook_time, difficulty, rating) values(?,?,?,?);", (name, cook_time, difficulty, rating))
    con.commit()
    con.close()

'''
Function for getting all recipes
USES: Most basic query
'''
def get_all_recipes():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("SELECT * from recipe;")
    recipes = cursor.fetchall()
    return recipes

'''
Function for getting vegetarian recipes.
USES: Left outer join
'''
def get_vegetarian_recipes():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("SELECT * from recipe r left join recipe_protein rp where rp.protein_id is null;")
    recipes = cursor.fetchall()
    return recipes