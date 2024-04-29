-- create database
create database product1;

-- create table
create sequence customer_id_serial start 1;
create table customer(
	customer_id bigint default nextval('customer_id_serial') primary key,
	first_name varchar(99),
	last_name varchar(99),
	birth_date date,
	address varchar(99),
	phone_number varchar(99),
	email varchar(99),
	job_title varchar(99),
	active_status int,
	created_datetime timestamp,
	updated_datetime timestamp
);

create sequence service_id_serial start 1;
create table service(
	service_id bigint default nextval('service_id_serial') primary key,
	name varchar(99),
	price decimal(38,5),
	image varchar(99),
	active_status int,
	created_datetime timestamp,
	updated_datetime timestamp
);

create sequence trans_id_serial start 1;
create table trans(
	trans_id bigint default nextval('trans_id_serial') primary key,
	customer_id bigint,
	service_id bigint,
	period_type_id int,
	amount decimal(38,5),
	review_score int,
	review_comment varchar(99),
	review_images varchar(99),
	created_datetime timestamp,
	updated_datetime timestamp
);

create sequence period_type_id_serial start 1;
create table period_type(
	period_type_id int default nextval('period_type_id_serial') primary key,
	period_type varchar(99),
	active_status int,
	created_datetime timestamp,
	updated_datetime timestamp
);