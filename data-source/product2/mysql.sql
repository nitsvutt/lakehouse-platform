
drop sequence product2.account_id_serial;
drop table product2.account;
drop sequence product2.product_id_serial;
drop table product2.product;
drop sequence product2.order_id_serial;
drop table product2.order;

create sequence product2.account_id_serial start 1;
create table product2.account(
	account_id bigint default nextval('account_id_serial') primary key,
	username varchar(99),
	password varchar(99),
	first_name varchar(99),
	last_name varchar(99),
	birth_date date,
	address varchar(99),
	phone_number varchar(99),
	email varchar(99),
	job_title varchar(99),
	updated_datetime timestamp
);

create sequence product2.product_id_serial start 1;
create table product2.product(
	product_id bigint default nextval('product_id_serial') primary key,
	name varchar(99),
	price decimal(38,5),
	image varchar(99),
	active_date date,
	inactive_date date,
	updated_datetime timestamp
);

create sequence product2.order_id_serial start 1;
create table product2.order(
	order_id bigint default nextval('order_id_serial') primary key,
	account_id bigint,
	product_id bigint,
	quantity int,
	recorded_date date,
	received_address varchar(99),
	received_datetime timestamp,
	received_image varchar(99),
	review_score int,
	review_comment varchar(99),
	review_images varchar(99),
	updated_datetime timestamp
);