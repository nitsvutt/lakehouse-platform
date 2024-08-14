drop table product2.account;
drop table product2.product;
drop table product2.order;

create table product2.account(
	account_id bigint auto_increment,
	username varchar(99),
	password varchar(99),
	first_name varchar(99),
	last_name varchar(99),
	birth_date date,
	address varchar(99),
	phone_number varchar(99),
	email varchar(99),
	job_title varchar(99),
	updated_datetime timestamp,
	primary key (account_id)
);

create table product2.product(
	product_id bigint auto_increment,
	name varchar(99),
	price decimal(38,5),
	image varchar(99),
	active_date date,
	inactive_date date,
	updated_datetime timestamp,
	primary key (product_id)
);

create table product2.order(
	order_id bigint auto_increment,
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
	updated_datetime timestamp,
	primary key (order_id)
);