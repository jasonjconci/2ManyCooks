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


def create_recipe_protein(recipe_name, protein_name):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("insert into recipe_protein (recipe_name, protein_name) values(?,?);", (recipe_name, protein_name))
    con.commit()
    con.close()


def create_recipe_vegetable(recipe_name, vegetable_name):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("insert into recipe_vegetable (recipe_name, vegetable_name) values(?,?);", (recipe_name, vegetable_name))
    con.commit()
    con.close()

def create_recipe_equipment(recipe_name, equipment_name):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("insert into recipe_equipment (recipe_name, equipment_name) values(?,?);", (recipe_name, equipment_name))
    con.commit()
    con.close()


def create_recipe_starch(recipe_name, starch_name):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("insert into recipe_starch (recipe_name, starch_name) values(?,?);", (recipe_name, starch_name))
    con.commit()
    con.close()

def create_recipe_instructions(recipe_name, instructions):
    instr_id = create_simple_instructions(instructions)
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("insert into recipe_instructions (recipe_name, instructions_id) values (?,?);", (recipe_name, instructions))
    con.commit()
    con.close()

def create_simple_instructions(instructions):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("insert into instructions (instructions_text) values (?);", (instructions))
    cursor.execute("select * from instructions where instructions_text = (?);", (instructions))
    instruction_id = cursor.fetchall()[0][0]
    con.commit()
    con.close()
    return instruction_id

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
    cursor.execute("SELECT r.rid from recipe r left join recipe_protein rp where rp.protein_id is null;")
    recipes = cursor.fetchall()
    return recipes

def get_recipe_with_id_protein(name):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("select * from recipe r join recipe_protein rp on(r.name = rp.recipe_name) join protein p on (p.name = rp.protein_name) where p.name = (?);", (name))
    recipes = cursor.fetchall()
    return recipe

'''
Functions for getting recipes containing a specific ingredient.
For example, get_recipes_with_* queries the * table, finding
all recipes using a given member of the * table.
USES: standard inner join
'''
### Function Block Begin ##
def get_recipes_with_protein(protein):
    cursor.execute("SELECT * from recipe r join recipe_protein rp on (r.id = rp.recipe_id) where rp.protein_id = (select id from protein where name=(?))", (protein))


def get_recipes_with_vegetable(veg):
    cursor.execute("SELECT * from recipe r join recipe_vegetable rp on (r.id = rp.recipe_id) where rp.vegetable = (select id from vegetable where name=(?))", (veg))

def get_recipes_with_starch(starch):
    cursor.execute("SELECT * from recipe r join recipe_starch rp on (r.id = rp.recipe_id) where rp.starch = (select id from starch where name=(?))", (starch))
### Function Block End ###

def delete_all_recipe_reviews(recipe_name):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("DELETE FROM review re WHERE re.id IN (SELECT rr.review_id FROM recipe r join recipe_review rr on (r.name = rr.recipe_name) WHERE r.name=(?)));", (recipe_name))
    cursor.execute("DELETE FROM recipe_review WHERE recipe_name=(?);", (recipe_name))
    con.commit()
    con.close()