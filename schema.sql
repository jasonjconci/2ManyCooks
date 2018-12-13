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
	name text primary key not null,
	cook_time integer not null,
	difficulty integer not null,
	rating integer not null
);

CREATE TABLE equipment (
	name text primary key
);

CREATE TABLE starch (
	name text primary key
);

CREATE TABLE vegetable  (
	name text primary key
);

CREATE TABLE protein  (
	name text primary key
);

CREATE TABLE instructions(
	id integer primary key,
	instructions text not null
);

CREATE TABLE review (
	id integer primary key,
	author text not null,
	body text not null,
	rating integer not null
);

CREATE TABLE recipe_review (
	recipe_name text not null,
	review_id integer not null,
	post_time text not null,
	foreign key (recipe_name) references recipe(name),
	foreign key (review_id) references review(id)
);

CREATE TABLE recipe_instructions (
	recipe_name text not null,
	instructions_id integer not null,
	foreign key (recipe_name) references recipe(name),
	foreign key (instructions_id) references instructions(id)
);


CREATE TABLE recipe_protein (
	recipe_name text not null,
	protein_name text not null,
	amount integer not null,
	foreign key (recipe_name) references recipe(name),
	foreign key (protein_name) references protein(name)
);

CREATE TABLE recipe_starch (
	recipe_name text not null,
	starch_name text not null,
	amount integer not null,
	foreign key (recipe_name) references recipe(name),
	foreign key (starch_name) references starch(name)
);

CREATE TABLE recipe_vegetable (
	recipe_name text not null,
	vegetable_name text not null,
	amount integer not null,
	foreign key (recipe_name) references recipe(name),
	foreign key (vegetable_name) references vegetable(name)
);


CREATE TABLE recipe_equipment (
	recipe_name text not null,
	equipment_name integer not null,
	foreign key (recipe_name) references recipe(name),
	foreign key (equipment_name) references equipment(name)
);

INSERT INTO protein VALUES ("steak"), ("chicken"), ("fish"), ("pork");
INSERT INTO vegetable VALUES ("corn"), ("potato"), ("onion"), ("celery"), ("carrot");
INSERT INTO starch VALUES ("brown rice"), ("white rice"), ("pasta"), ("bread");
INSERT INTO equipment VALUES ("blender"), ("mixer"), ("stove"), ("microwave"), ("oven");