drop table customer;
drop sequence customer_id_serial;
drop table service;
drop sequence service_id_serial;
drop table period;
drop sequence period_id_serial;
drop table trans;
drop sequence trans_id_serial;
drop table review;
drop sequence review_id_serial;

create sequence customer_id_serial start 1;
create table customer(
	customer_id bigint default nextval('customer_id_serial') primary key,
	first_name varchar(99),
	last_name varchar(99),
	birth_date date,
	address varchar(99),
	phone_number varchar(99) not null,
	email varchar(99),
	job_title varchar(99),
	updated_datetime timestamp
);

create sequence service_id_serial start 1;
create table service(
	service_id bigint default nextval('service_id_serial') primary key,
	name varchar(99) not null,
	price decimal(38,5),
	image varchar(99),
	active_date date,
	inactive_date date,
	is_active int,
	updated_datetime timestamp
);

create sequence period_id_serial start 1;
create table period(
	period_id bigint default nextval('period_id_serial') primary key,
	name varchar(99) not null,
	factor decimal(38,5),
	extra decimal(38,5),
	active_date date,
	inactive_date date,
	is_active int,
	updated_datetime timestamp
);

create sequence trans_id_serial start 1;
create table trans(
	trans_id bigint default nextval('trans_id_serial') primary key,
	customer_id bigint,
	service_id bigint,
	period_id bigint,
	recorded_date date,
	updated_datetime timestamp
);

create sequence review_id_serial start 1;
create table review(
	review_id bigint default nextval('review_id_serial') primary key,
	trans_id bigint,
	score int,
	comment varchar(99),
	image varchar(99),
	updated_datetime timestamp
);