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
###BEGIN FUNCTION BLOCK FOR CREATING NEW RECIPE###
def create_recipe(name, cook_time, difficulty):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("insert into recipe (name, cook_time, difficulty) values(?,?,?);", (name, cook_time, difficulty))
    con.commit()
    con.close()

def create_recipe_protein(recipe_name, protein_name, amount):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("insert into recipe_protein (recipe_name, protein_name, amount) values(?,?,?);", (recipe_name, protein_name, amount))
    con.commit()
    con.close()

def create_recipe_vegetable(recipe_name, vegetable_name, amount):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("insert into recipe_vegetable (recipe_name, vegetable_name, amount) values(?,?,?);", (recipe_name, vegetable_name, amount))
    con.commit()
    con.close()

def create_recipe_starch(recipe_name, starch_name, amount):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("insert into recipe_starch (recipe_name, starch_name, amount) values(?,?,?);", (recipe_name, starch_name, amount))
    con.commit()
    con.close()

    
def create_recipe_equipment(recipe_name, equipment_name):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("insert into recipe_equipment (recipe_name, equipment_name) values(?,?);", (recipe_name, equipment_name))
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
    cursor.execute("insert into instructions (instructions_text) values (?);", (instructions,))
    cursor.execute("select * from instructions where instructions_text = (?);", (instructions,))
    instruction_id = cursor.fetchall()[0][0]
    con.commit()
    con.close()
    return instruction_id

### END FUNCTION BLOCK FOR RECIPE CREATION ###

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

def get_all_recipe_information(recipe_name):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("SELECT * from recipe r where name=(?);", (recipe_name,))
    r = cursor.fetchall()
    cursor.execute("SELECT rp.* from recipe r join recipe_protein rp on (r.name = rp.recipe_name) where r.name=(?);", (recipe_name,))
    rp = cursor.fetchall()
    cursor.execute("SELECT rv.* FROM recipe r join recipe_vegetable rv on (r.name = rv.recipe_name) where r.name=(?);", (recipe_name,))
    rv = cursor.fetchall()
    cursor.execute("SELECT rs.* FROM recipe r join recipe_starch rs on (r.name = rs.recipe_name) where r.name=(?);", (recipe_name,))
    rs = cursor.fetchall()
    cursor.execute("SELECT re.* FROM recipe r join recipe_equipment re on (r.name = re.recipe_name) where r.name=(?);", (recipe_name,))
    re = cursor.fetchall()
    cursor.execute("SELECT ri.* FROM recipe r join recipe_instructions ri on (r.name = ri.recipe_name) where r.name=(?);", (recipe_name,))
    ri = cursor.fetchall()
    return [r, rp, rv, rs, re, ri]


def query_builder(name, difficulty, protein, vegetable, starch, vegetarian, equip_list):
    built_query = ''
    if name != '':
        built_query += get_recipe_with_name(name)
        built_query += ' INTERSECT '
    if difficulty:
        print("Got difficulty")
        built_query += get_recipe_max_difficity(difficulty)
        built_query += ' INTERSECT '
    if protein != 'none':
        print("got protein")
        built_query += get_recipes_with_protein(protein)
        built_query += ' INTERSECT '
    if vegetable != 'none':
        print("Got veg")
        built_query += get_recipes_with_vegetable(vegetable)
        built_query += ' INTERSECT '
    if starch != 'none':
        print("got starch")
        built_query += get_recipes_with_starch(starch)
        built_query += ' INTERSECT '
    if len(vegetarian) > 0:
        built_query += get_vegetarian_recipes()
        built_query += ' INTERSECT '
    for equip in equip_list:
        built_query += get_recipe_without_equipment(equip)
        built_query += ' INTERSECT '
    built_query = built_query[:-11]
    built_query += ';'
    print(built_query)
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute(built_query)
    results = cursor.fetchall()
    return results

'''
Functions for getting recipes containing a specific ingredient.
For example, get_recipes_with_* queries the * table, finding
all recipes using a given member of the * table.
USES: standard inner join
'''
### Function Block Begin ##
def get_recipe_with_name(name):
    return "SELECT r.* from recipe r where name like \'%" + name + "%\'"

def get_recipes_with_protein(protein):
    return "SELECT r.* from recipe r join recipe_protein rp on (r.name = rp.recipe_name) where rp.protein_name = \'" + protein + "\'"

def get_recipes_with_vegetable(veg):
    return "SELECT r.* from recipe r join recipe_vegetable rv on (r.name = rv.recipe_name) where rv.vegetable_name = \'" + veg + "\'"

def get_recipes_with_starch(starch):
    return "SELECT r.* from recipe r join recipe_starch rs on (r.name = rs.recipe_name) where rs.starch_name = \'" + starch + "\'"
### Function Block End ###

def get_vegetarian_recipes():
    return "SELECT r.* from recipe r left join recipe_protein rp on (r.name = rp.recipe_name) where rp.protein_name is null"

def get_recipe_max_difficity(difficulty):
    return "SELECT r.* from recipe r where difficulty < " + difficulty

def get_recipe_without_equipment(equip):
    return "SELECT r.* from recipe r join recipe_equipment re on (r.name = re.recipe_name) where re.equipment_name != \'" + equipment + "\'"





def delete_recipe(recipe_name):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    delete_all_recipe_reviews(recipe_name)
    cursor.execute("DELETE FROM recipe_instructions WHERE recipe_name=(?);", (recipe_name,))
    cursor.execute("DELETE FROM recipe_equipment WHERE recipe_name=(?);", (recipe_name,))
    cursor.execute("DELETE FROM recipe_vegetable WHERE recipe_name=(?);", (recipe_name,))
    cursor.execute("DELETE FROM recipe_starch WHERE recipe_name=(?);", (recipe_name,))
    cursor.execute("DELETE FROM recipe_protein WHERE recipe_name=(?);", (recipe_name,))
    cursor.execute("DELETE FROM recipe WHERE name=(?);", (recipe_name,))
    con.commit()
    con.close()

'''
Function for deleting recipe reviews and recipe_review relationships connecting the two.
USES: Subqueries
'''
def delete_all_recipe_reviews(recipe_name):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cursor = con.cursor()
    cursor.execute("DELETE FROM review WHERE id IN (SELECT rr.review_id FROM recipe r join recipe_review rr on (r.name = rr.recipe_name) WHERE r.name=(?));", (recipe_name,))
    cursor.execute("DELETE FROM recipe_review WHERE recipe_name=(?);", (recipe_name,))
    con.commit()
    con.close()


