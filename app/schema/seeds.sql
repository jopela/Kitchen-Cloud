-- sql data that needs to be preloaded inside the database before starting the
-- application. Currently only used for testing.

-- insert the supported statuses in the database.
insert into status (id, name) values ('1',"ACTIVE");
insert into status (id, name) values ('2',"BLOCKED");

-- create a person 2 person for testing (a real and a fake one). The real one 
-- could be used to test the sending of mails for example.
insert into person (id, firstname, lastname, email) values ('1','Brian','Murdock','bmurdock@example.com');

insert into person (id, firstname, lastname, email) values ('2','Jonathan','Pelletier','jonathan.pelletier1@gmail.com');

-- Add user accounts associated with the previous persons.
insert into user (id, username, hash, person, status) values ('1','jopela','hashhashhash','2','1');
