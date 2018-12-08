/*
This file is for the creation of clean tables, for the schema
defined within this project. Namely, based on creation of ER
diagrams, we have tables pertaining to actual data storage
(entities), and tables pertaining to connecting data tables
(relationships). All relationship tables are named with
an underscore between the tables they connect, while entities
are single-word table names.
*/

DROP TABLE IF EXISTS recipe_review;
DROP TABLE IF EXISTS recipe_vegetable;
DROP TABLE IF EXISTS recipe_protein;
DROP TABLE IF EXISTS recipe_starch;
DROP TABLE IF EXISTS recipe_equipment;
DROP TABLE IF EXISTS recipe_instructions;

DROP TABLE IF EXISTS review;
DROP TABLE IF EXISTS instructions;
DROP TABLE IF EXISTS protein;
DROP TABLE IF EXISTS vegetable;
DROP TABLE IF EXISTS starch;
DROP TABLE IF EXISTS equipment;

DROP TABLE IF EXISTS recipe;


CREATE TABLE recipe (
	id integer primary key autoincrement,
	name text not null,
	cook_time integer not null,
	difficulty integer not null,
	rating integer not null
);

CREATE TABLE equipment (
	id integer primary key autoincrement,
	name text not null
);

CREATE TABLE starch (
	id integer primary key autoincrement,
	name text not null
);

CREATE TABLE vegetable  (
	id integer primary key autoincrement,
	name text not null
);

CREATE TABLE protein  (
	id integer primary key autoincrement,
	name text not null
);

CREATE TABLE instructions(
	id integer primary key autoincrement,
	instructions text not null
);

CREATE TABLE review (
	id integer primary key autoincrement,
	author text not null,
	body text not null,
	rating integer not null
);

CREATE TABLE recipe_review (
	recipe_id integer not null,
	review_id integer not null,
	post_time text not null,
	foreign key (recipe_id) references recipe(id),
	foreign key (review_id) references review(id)
);

CREATE TABLE recipe_instructions (
	recipe_id integer not null,
	instructions_id integer not null,
	foreign key (recipe_id) references recipe(id),
	foreign key (instructions_id) references instructions(id)
);


CREATE TABLE recipe_protein (
	recipe_id integer not null,
	protein_id integer not null,
	amount integer not null,
	foreign key (recipe_id) references recipe(id),
	foreign key (protein_id) references protein(id)
);

CREATE TABLE recipe_starch (
	recipe_id integer not null,
	starch_id integer not null,
	amount integer not null,
	foreign key (recipe_id) references recipe(id),
	foreign key (starch_id) references starch(id)
);

CREATE TABLE recipe_vegetable (
	recipe_id integer not null,
	vegetable_id integer not null,
	amount integer not null,
	foreign key (recipe_id) references recipe(id),
	foreign key (vegetable_id) references vegetable(id)
);


CREATE TABLE recipe_equipment (
	recipe_id integer not null,
	equipment_id integer not null,
	foreign key (recipe_id) references recipe(id),
	foreign key (equipment_id) references equipment(id)
);

INSERT INTO protein VALUES ("steak"), ("chicken"), ("fish"), ("pork");
INSERT INTO vegetable VALUES ("corn"), ("potato"), ("onion"), ("celery"), ("carrot");
INSERT INTO starch VALUES ("brown rice"), ("white rice"), ("pasta"), ("bread");
INSERT INTO equipment VALUES ("blender"), ("mixer"), ("stove"), ("microwave"), ("oven");