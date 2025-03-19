show databases;
create database if not exists second_example;
use second_example;

create table person(
	person_id smallint unsigned,
    fname varchar(20),
    lname varchar(20),
    gender enum('M', 'F'),
    birth_date date,
    street varchar(30),
    city varchar(20),
    state varchar(20),
    country varchar(20),
    portal_code varchar (20),
    constraint pk_person primary key (person_id)
);

desc person;

create table favorite_food(
	person_id smallint unsigned,
    food varchar(20),
    constraint pk_favorite_food primary key (person_id, food),
    constraint fk_favorite_food_person_id foreign key (person_id) references person(person_id)
);

desc favorite_food;

#pegar constraints
show databases;
desc information_schema.table_constraints;
select * from information_schema.table_constraints where constraint_schema = 'second_example';
select * from information_schema.table_constraints where table_name = 'person';

desc person;
insert into person values('0', 'Carolina', 'Silva', 'F', '1979-08-21', 'rua tal', 'cidade j', 'RJ', 'Brasil', '26054-89');
insert into person values('1', 'Luiz', 'Silva', 'M', '1979-08-21', 'rua tal', 'cidade j', 'RJ', 'Brasil', '26054-89'),
						 ('2', 'Roberta', 'Silva', 'F', '1979-08-21', 'rua tal', 'cidade j', 'RJ', 'Brasil', '26054-89');

select * from person;
delete from person where person_id = 1 or person_id = 2;
select * from person;

desc favorite_food;
insert into favorite_food values (0,'lasanha'),
								 (1,'carne assada'),
                                 (2,'fetuccine');
select * from favorite_food;