'''
# This file contains all SQL-querying aspects of our project.
# Within this file are all queries, query-building, and query
# using methods. Documentation for each method found above the
# declaration, as well as documentation as to what aspect of SQL
# is used (insert, selects, joins, subqueries, etc.)
'''

import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))

'''
Function for adding a recipe to our database's recipe table.
USES: insert
'''
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
    cursor.execute("select * from recipe;")
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


'''
Functions for getting recipes containing a specific ingredient.
For example, get_recipes_with_* queries the * table, finding
all recipes using a given member of the * table.
USES: standard inner join
'''
### Function Block Begin ##
def get_recipes_with_protein(protein):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("SELECT * from recipe r join recipe_protein rp on (r.id = rp.recipe_id) where rp.protein_id = (select id from protein where name=(?))", (protein))
    recipes = cursor.fetchall()
    return recipes

def get_recipes_with_vegetable(veg):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("SELECT * from recipe r join recipe_vegetable rp on (r.id = rp.recipe_id) where rp.vegetable = (select id from vegetable where name=(?))", (veg))
    recipes = cursor.fetchall()
    return recipes

def get_recipes_with_starch(starch):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("SELECT * from recipe r join recipe_starch rp on (r.id = rp.recipe_id) where rp.starch = (select id from starch where name=(?))", (starch))
    recipes = cursor.fetchall()
    return recipes

def get_recipe_with_id(id):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("select * from recipe r join recipe_protein rp on(r.id = rp.recipe_id) join protein p on (p.id = rp.protein_id) where r.id = (?);", (id))
    recipes = cursor.fetchall()
    return recipe
### Function Block End ###