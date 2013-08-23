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

-- User of the application. Pays (hopefully) something to use our app.
-- will later need to add payment info to a user but this is for the future ...
create table user (
    id integer primary key,
    username varchar(254),
    hash varchar(120),
    person integer unique,
    foreign key(person) references person(id)
);

-- Kitchen owned by a user. User may have many kitchen
create table kitchen (
    id integer primary key,
    name varchar(20),
    owner integer,
    foreign key(owner) references user(id)
);

-- Grocer. Can be food from them
-- TODO: need to add grocer_person table, grocer_product table.
create table grocer (
    id integer primary key,
    name varchar(30),
    account varchar(30)
);

-- Product. Things that can be bought from food grocers.



