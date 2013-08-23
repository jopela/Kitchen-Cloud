-- Kitchen-Cloud datamodel.

-- User of the application.
create table user (
    id integer primary key,
    username varchar(254),
    email varchar(254) unique,
    -- sha512 password hash.
    hash varchar(120)
);

-- Kitchen owned by user.
create table kitchen (
    id integer primary key,
    name varchar(20),
    owner integer,
    foreign key(owner) references user(id)
);

-- Grocer.
--create table grocer (



-- Product. Things that can be bought from food grocers.


-- Zone where food is stored inside the Kitchen
--create table zone (
--    name varchar(30),



