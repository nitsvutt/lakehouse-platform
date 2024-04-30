create sequence customer_system_id_serial start 1;
create sequence customer_id_serial start 1;
create table customer(
	system_id bigint default nextval('customer_system_id_serial') primary key,
	customer_id bigint default nextval('customer_id_serial'),
	first_name varchar(99),
	last_name varchar(99),
	birth_date date,
	address varchar(99),
	phone_number varchar(99),
	email varchar(99),
	job_title varchar(99),
	active_date date,
	inactive_date date,
	created_datetime timestamp,
	updated_datetime timestamp
);
create table customer_hist(
	system_id bigint primary key,
	customer_id bigint,
	first_name varchar(99),
	last_name varchar(99),
	birth_date date,
	address varchar(99),
	phone_number varchar(99),
	email varchar(99),
	job_title varchar(99),
	active_date date,
	inactive_date date,
	created_datetime timestamp,
	updated_datetime timestamp
);

create sequence service_system_id_serial start 1;
create sequence service_id_serial start 1;
create table service(
	system_id bigint default nextval('service_system_id_serial') primary key,
	service_id bigint default nextval('service_id_serial'),
	name varchar(99),
	price decimal(38,5),
	image varchar(99),
	active_date date,
	inactive_date date,
	created_datetime timestamp,
	updated_datetime timestamp
);
create table service_hist(
	system_id bigint primary key,
	service_id bigint,
	name varchar(99),
	price decimal(38,5),
	image varchar(99),
	active_date date,
	inactive_date date,
	created_datetime timestamp,
	updated_datetime timestamp
);

create sequence period_system_id_serial start 1;
create sequence period_id_serial start 1;
create table period(
	system_id bigint default nextval('period_system_id_serial') primary key,
	period_id bigint default nextval('period_id_serial'),
	name varchar(99),
	factor decimal(38,5),
	extra decimal(38,5),
	active_date date,
	inactive_date date,
	created_datetime timestamp,
	updated_datetime timestamp
);
create table period_hist(
	system_id bigint primary key,
	period_id bigint,
	name varchar(99),
	factor decimal(38,5),
	extra decimal(38,5),
	active_date date,
	inactive_date date,
	created_datetime timestamp,
	updated_datetime timestamp
);

create sequence trans_system_id_serial start 1;
create sequence trans_id_serial start 1;
create table trans(
	system_id bigint default nextval('trans_system_id_serial') primary key,
	trans_id bigint default nextval('trans_id_serial'),
	customer_id bigint,
	service_id bigint,
	period_id bigint,
	recorded_date date,
	created_datetime timestamp,
	updated_datetime timestamp
);

create sequence review_system_id_serial start 1;
create sequence review_id_serial start 1;
create table review(
	system_id bigint default nextval('review_system_id_serial') primary key,
	review_id bigint default nextval('review_id_serial'),
	trans_id bigint,
	score int,
	comment varchar(99),
	image varchar(99),
	created_datetime timestamp,
	updated_datetime timestamp
);
create table review_hist(
	system_id bigint primary key,
	review_id bigint,
	trans_id bigint,
	score int,
	comment varchar(99),
	image varchar(99),
	created_datetime timestamp,
	updated_datetime timestamp
);