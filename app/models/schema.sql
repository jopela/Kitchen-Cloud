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
    person integer unique,
    status integer,
    foreign key(person) references person(id),
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
    name varchar(30)
);

-- Grocer. Can purchase food from them
create table grocer (
    id integer primary key,
    name varchar(30),
    account varchar(30)
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
    name varchar(30),
    description varchar(100),
    category integer,
    price float,
    kitchen integer,
    foreign key(category) references category(id),
    foreign key(kitchen) references kitchen(id)
);

-- Waste. Represents the waste coefficent for a transformation applied to a
-- food product (e.g: peeled carrot vs non-peeled carots. With peeled carots,
-- you have greater waste.).
create table waste (
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
    quantity float,
    product integer,
    foreign key(product) references product(id)
);
    

