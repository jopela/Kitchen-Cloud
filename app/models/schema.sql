-- Kitchen-Cloud datamodel.

-- Person, can be called by name and yelled at.
create table person (
    id integer primary key, 
    name varchar(50),
    email varchar(254) unique
);

-- Telephone, something that can be typed on a phone to yell at someone.
create table telephone (
    id integer primary key,
    num varchar(50),
    owner integer,
    foreign key(owner) references person(id)
);

-- Status. For account statuses (e.g: blocked, active, payment pending etc.).
create table status (
    id integer primary key,
    name varchar(30)
);

-- User of the application. Pays (hopefully) something to use our app.
-- will later need to add payment info to a user but this is for the future ...
create table user (
    id integer primary key,
    username varchar(254),
    hash varchar(120),
    owner integer unique,
    status integer,
    foreign key(owner) references person(id),
    foreign key(status) references status(id)
);

-- Kitchen owned by a user. User may have many kitchens
create table kitchen (
    id integer primary key,
    name varchar(20),
    owner integer,
    foreign key(owner) references user(id)
);

-- Category. This is for food item category (e.g: VEGETABLE, MEAT, CEREAL).
create table category (
    id integer primary key,
    name varchar(30),
    user integer,
    foreign key(user) references user(id)
);

-- Grocer. Can purchase food from them
create table grocer (
    id integer primary key,
    name varchar(30),
    account_number varchar(30),
    user integer,
    foreign key(user) references user(id)

);

-- Enables the many-to-many relationship between grocer and products (e.g: many
-- grocers may sell potatoes and many products may be sold by one grocer).
create table grocer_product (
    grocer_id integer,
    product_id integer,
    foreign key(grocer_id) references grocer(id),
    foreign key(product_id) references product(id),
    primary key(grocer_id, product_id)
);

-- Enables the many-to-many relationship between grocer and person (e.g: a 
-- grocer may have many 
create table grocer_person (
    grocer_id integer,
    person_id integer,
    foreign key(grocer_id) references grocer(id),
    foreign key(person_id) references person(id),
    primary key(grocer_id, person_id)
);

-- Zone. Places where you store your food. A kitchen is a collection
-- of Zones.
create table zone (
    id integer primary key,
    name varchar(30),
    kitchen integer,
    foreign key(kitchen) references kitchen(id)
);

-- Product. Things that can be bought from food grocers.
create table product(
    id integer primary key,
    name varchar(30) unique,
    description varchar(100),
    category integer,
    price float,
    foreign key(category) references category(id)
);

-- Quantity. A measure of how much of a particular foor product
-- you have at a particular date and where it is stored (zone).
create table quantity(
    id integer primary key,
    zone integer,
    format integer,
    timestamp date,
    numerical float, -- quantity stored.
    foreign key(zone) references zone(id),
    foreign key(format) references format(id)
);

-- Transformation. Represents the waste coefficent for a transformation applied to a
-- food product during meal preparation (e.g: peeled carrot vs non-peeled 
-- carots).
create table transformation(
    id integer primary key,
    name varchar(20),
    coefficient float,
    product integer,
    foreign key(product) references product(id)
);

-- Format. Units and quantity in that unit that are worth a product price.
-- This is used to state that, example, 1 KG of carrots, 1000 g of carrots and
-- ~ 120 individuals carrots are worth, say, 24$. 
create table format (
    id integer primary key,
    name varchar(30),
    unit varchar(20),
    quantity integer,
    product integer,
    foreign key(product) references product(id)
);

-- Invoice. All food purchases made at a particular grocer. 
create table invoice (
    id integer primary key,
    timestamp date,
    grocer integer,
    kitchen integer,
    foreign key(kitchen) references kitchen(id),
    foreign key(grocer) references grocer(id)

);

-- Items that can be found on an invoice.
create table invoice_product(
    id integer primary key,
    product integer,
    invoice integer,
    format integer,
    quantity integer,
    price float,

    foreign key(product) references product(id),
    foreign key(invoice) references invoice(id),
    foreign key(format) references format(id)

);

-- Recipe. List of product found in a receipe.
create table recipe (
    id integer primary key,
    description varchar(50),
    user integer,
    nbr_meals integer,

    foreign key(user) references user(id)
);

-- Enables the many-to-many relationship between recipe and kitchen.
 create table recipe_kitchen (
    recipe integer,
    kitchen integer,
    foreign key(recipe) references recipe(id),
    foreign key(kitchen) references Kitchen(id),
    primary key(recipe, kitchen)
);

--Enables the many-to-many relationship between product and recipes. This 
-- relationship as attributes such as transformation, format and quantity.
create table recipe_product (
    id integer primary key,

    recipe integer,
    product integer,
    transformation integer,
    format integer,

    quantity integer,

    foreign key(recipe) references recipe(id),
    foreign key(product) references product(id),
    unique(recipe, product, transformation, format)
);









