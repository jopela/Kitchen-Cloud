-- Kitchen-Cloud datamodel.

-- Person. Superclass for user and contact.
create table person (
    id integer primary key, 
    firstname varchar(50),
    lastname varchar(50),
    email varchar(254) unique

);

-- User of the application. A subtype of person who pays (hopefully) something 
-- to use our app. Will later need to add payment info to a user but this is 
-- for the future ...
create table user (
    id integer primary key,
    username varchar(254) unique,
    hash varchar(120),
    person integer unique,
    status integer,
    foreign key(person) references person(id),
    foreign key(status) references status(id)
);

-- A list of all the user that are currently in the authenticated state. This
-- is required to implement user login.
create table authenticated (
    id integer primary key,
    foreign key(id) references user(id)
);

-- Contact. A subtype  of person that represent the communication 
-- point with a grocer.
create table contact (
    id integer primary key,
    job_title varchar(50),

    person integer unique,
    user integer,

    foreign key(user) references user(id), -- user that entered the contact 
    -- info.
    foreign key(person) references person(id)
);

-- Telephone, something that can be typed on a phone to yell at someone.
create table telephone (
    id integer primary key,
    num varchar(50),
    owner integer,
    foreign key(owner) references person(id)
);

-- Status. For account statuses (e.g: blocked, active, payment pending etc.).
-- This table is application wide (same value used by all app users).
create table status (
    id integer primary key,
    name varchar(30)
);

-- Kitchen owned by a user. User may have many kitchens
create table kitchen (
    id integer primary key,
    name varchar(20),
    user integer,
    foreign key(user) references user(id)
);

-- Category. This is for food item category (e.g: VEGETABLE, MEAT, CEREAL).
create table category (
    id integer primary key,
    name varchar(30),
    user integer, -- each user may setup categories for all of it's kitchens.
    foreign key(user) references user(id)
);

-- Grocer. Can purchase food from them
create table grocer (
    id integer primary key,
    name varchar(30),
    account_number varchar(30),
    user integer, -- each user has it's set of grocer.
    foreign key(user) references user(id)

);

-- Enables the many-to-many relationship between grocer and products (e.g: many
-- grocers may sell potatoes and many products may be sold by one grocer).
create table grocer_product (
    grocer integer,
    product integer,
    foreign key(grocer) references grocer(id),
    foreign key(product) references product(id),
    primary key(grocer, product)
);

-- Enables the many-to-many relationship between grocer and contact (e.g: a 
-- grocer may have many contact and the same contact may be the same for
-- different grocers).
create table grocer_contact (
    grocer integer,
    contact integer,
    foreign key(grocer) references grocer(id),
    foreign key(contact) references contact(id),
    primary key(grocer, contact)
);

-- Zone. Places where you store your food. A kitchen is a collection
-- of Zones.
create table zone (
    id integer primary key,
    name varchar(30),
    kitchen integer,
    foreign key(kitchen) references kitchen(id)
);

-- Product. Things that can be bought from grocers.
create table product(
    id integer primary key,
    name varchar(30) unique,
    description varchar(100),
    category integer,
    price float,
    foreign key(category) references category(id)
);

-- Quantity. A measure of how much of a particular food product
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

-- Transformation. Represents the waste coefficent for a transformation applied 
-- to a food product during meal preparation (e.g: peeled carrot vs non-peeled 
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
    product integer, -- product to witch it applies.
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
    user integer, -- recipe belong to a particular user.
    nbr_meals integer,

    foreign key(user) references user(id)
);

-- Enables the many-to-many relationship between recipe and kitchen. Usefull
-- Because inventory is made by kitchen.
 create table recipe_kitchen (
    recipe integer,
    kitchen integer,
    foreign key(recipe) references recipe(id),
    foreign key(kitchen) references Kitchen(id),
    primary key(recipe, kitchen)
);

-- Enables the many-to-many relationship between product and recipes. This 
-- relationship has attributes such as transformation, format and quantity.
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


