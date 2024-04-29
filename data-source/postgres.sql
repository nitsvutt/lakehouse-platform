-- create database
create database product1;

-- create table
create table customer(
	customer_id bigint NOT NULL PRIMARY KEY,
	first_name varchar(99),
	last_name varchar(99),
	birth_date date,
	address varchar(99),
	phone_number varchar(99),
	email varchar(99),
	job_title varchar(99),
	created_datetime timestamp,
	updated_datetime timestamp
);
create sequence customer_id_serial start 1;

create table service(
	service_id bigint NOT NULL PRIMARY KEY,
	name varchar(99) NOT NULL,
	price decimal(38,5),
	image varchar(99) NOT NULL,
	created_datetime timestamp,
	updated_datetime timestamp
);
create sequence service_id_serial start 1;

create table trans(
	trans_id bigint NOT NULL PRIMARY KEY,
	customer_id bigint NOT NULL,
	service_id bigint NOT NULL,
	period_type_id int NOT NULL,
	review_score int,
	review_comment varchar(99),
	review_images varchar(99),
	created_datetime timestamp,
	updated_datetime timestamp
);
create sequence trans_id_serial start 1;

create table period_type(
	period_type_id int NOT NULL PRIMARY KEY,
	period_type varchar(99),
	created_datetime timestamp,
	updated_datetime timestamp
);
create sequence period_type_id_serial start 1;