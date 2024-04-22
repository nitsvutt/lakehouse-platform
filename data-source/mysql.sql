-- create database
create database product2;

-- create table
create table product2.account(
	account_id bigint NOT NULL PRIMARY KEY,
	username varchar(99) NOT NULL,
	password varchar(99) NOT NULL,
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

create table product2.product(
	product_id bigint NOT NULL PRIMARY KEY,
	name varchar(99) NOT NULL,
	price decimal(38,5),
	image varchar(99) NOT NULL,
	created_datetime timestamp,
	updated_datetime timestamp
);

create table product2.order(
	order_id bigint NOT NULL PRIMARY KEY,
	account_id bigint NOT NULL,
	product_id bigint NOT NULL,
	quantity int,
	received_address varchar(99),
	received_datetime timestamp,
	received_image varchar(99),
	review_score int,
	review_comment varchar(99),
	review_images varchar(99),
	created_datetime timestamp,
	updated_datetime timestamp
);