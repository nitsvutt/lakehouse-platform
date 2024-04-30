-- create database
create database product1;

-- create table
create sequence customer_id_serial start 1;
create table customer(
	customer_id bigint default nextval('customer_id_serial'),
	first_name varchar(99),
	last_name varchar(99),
	birth_date date,
	address varchar(99),
	phone_number varchar(99),
	email varchar(99),
	job_title varchar(99),
	active_status int,
	active_date date,
	inactive_date date,
	created_datetime timestamp,
	updated_datetime timestamp
);

create sequence service_id_serial start 1;
create table service(
	service_id bigint default nextval('service_id_serial'),
	name varchar(99),
	price decimal(38,5),
	image varchar(99),
	active_status int,
	active_date date,
	inactive_date date,
	created_datetime timestamp,
	updated_datetime timestamp
);

create sequence period_id_serial start 1;
create table period(
	period_id int default nextval('period_id_serial'),
	name varchar(99),
	factor decimal(38,5),
	extra decimal(38,5),
	active_status int,
	active_date date,
	inactive_date date,
	created_datetime timestamp,
	updated_datetime timestamp
);

create sequence trans_id_serial start 1;
create table trans(
	trans_id bigint default nextval('trans_id_serial'),
	customer_id bigint,
	service_id bigint,
	period_id int,
	effect_date date,
	created_datetime timestamp,
	updated_datetime timestamp
);

create sequence review_id_serial start 1;
create table review(
	review_id bigint default nextval('review_id_serial'),
	trans_id bigint,
	score int,
	comment varchar(99),
	image varchar(99),
	posted_datetime date,
	created_datetime timestamp,
	updated_datetime timestamp
);