set autocommit = 0;

start transaction;

create database shop;
use shop;

create user 'app1'@'localhost' identified by 'Password123';
grant all on shop.* to 'app1';

create table category(
	id int primary key auto_increment,
    name varchar(32) not null
);

create table product(
	id int primary key auto_increment,
    category_id int not null,
    name varchar(32) not null,
    price decimal(7, 2) not null,
    in_stock bool not null,
    constraint fk_category_id foreign key(category_id) references category(id),
    constraint positive_price check(price > 0)
);

create table customer(
	id int primary key auto_increment,
    first_name varchar(32) not null,
    last_name varchar(32) not null,
    email varchar(64) not null,
    city varchar(64) not null,
    street varchar(64) not null,
    postal_code varchar(5) not null
);

create table order_details(
	id int primary key auto_increment,
    customer_id int not null,
    order_date datetime not null,
    payment enum('kreditni karta', 'hotovost') not null,
    constraint fk_customer_id foreign key(customer_id) references customer(id)
);

create table order_item(
	id int primary key auto_increment,
    product_id int not null,
    order_id int not null,
    amount int not null,
    constraint fk_product_id foreign key(product_id) references product(id),
    constraint fk_order_id foreign key(order_id) references order_details(id),
    constraint positive_amount check(amount >= 0)
);

create view products_out_of_stock as
select *
from product p
where p.in_stock = false;

create view total_sales as
select p.name, nvl(sum(i.amount * p.price), 0) as total_sales
from product p left join order_item i on i.product_id = p.id
group by p.name;

create view order_items
as
select d.id, c.first_name, c.last_name, d.order_date, d.payment, i.id item_id, p.name, p.price, i.amount
from order_details d inner join order_item i on i.order_id = d.id
inner join product p on i.product_id = p.id
inner join customer c on d.customer_id = c.id
order by d.id;

select * from order_items;

insert into category(name) values('Potraviny');
insert into category(name) values('Napoje');
insert into category(name) values('Elektronika');

insert into product(category_id, name, price, in_stock) values(1, 'Chleba', 14.90, true);
insert into product(category_id, name, price, in_stock) values(3, 'Baterie', 4.90, true);
insert into product(category_id, name, price, in_stock) values(2, 'Voda', 9.90, true);
insert into product(category_id, name, price, in_stock) values(2, 'Caj', 19.90, false);
insert into product(category_id, name, price, in_stock) values(1, 'Mrkev', 4.90, false);
insert into product(category_id, name, price, in_stock) values(1, 'Jablko', 3.90, true);
insert into product(category_id, name, price, in_stock) values(3, 'Graficka karta', 14990.00, false);
insert into product(category_id, name, price, in_stock) values(2, 'Kava', 24.90, true);
insert into product(category_id, name, price, in_stock) values(1, 'Pomeranc', 6.90, true);
insert into product(category_id, name, price, in_stock) values(3, 'Procesor', 9990.00, false);

insert into customer(first_name, last_name, email, city, street, postal_code) values('Dan', 'Zeleny', 'danzeleny@gmail.com', 'Praha', 'Jecna 40', '10034');
insert into customer(first_name, last_name, email, city, street, postal_code) values('Lukas', 'Modry', 'modry@gmail.com', 'Brno', 'Lomena 134', '56783');
insert into customer(first_name, last_name, email, city, street, postal_code) values('Jiri', 'Strom', 'jstrom@gmail.com', 'Ostrava', 'Nadrazni 6', '28934');
insert into customer(first_name, last_name, email, city, street, postal_code) values('Petr', 'Novak', 'novak@gmail.com', 'Brno', 'U Potoka 163', '56103');

insert into order_details(customer_id, order_date, payment) values(1, '2022-6-24 13:05:34', 'kreditni karta');
insert into order_details(customer_id, order_date, payment) values(3, '2022-6-24 14:37:02', 'kreditni karta');
insert into order_details(customer_id, order_date, payment) values(2, '2022-6-24 16:55:44', 'hotovost');
insert into order_details(customer_id, order_date, payment) values(1, '2022-6-25 08:25:14', 'kreditni karta');
insert into order_details(customer_id, order_date, payment) values(4, '2022-6-25 10:01:59', 'hotovost');
insert into order_details(customer_id, order_date, payment) values(2, '2022-6-25 11:09:41', 'kreditni karta');
insert into order_details(customer_id, order_date, payment) values(4, '2022-6-25 15:38:19', 'kreditni karta');
insert into order_details(customer_id, order_date, payment) values(3, '2022-6-26 07:42:04', 'hotovost');

insert into order_item(product_id, order_id, amount) values(3, 1, 3);
insert into order_item(product_id, order_id, amount) values(6, 1, 5);
insert into order_item(product_id, order_id, amount) values(1, 2, 2);
insert into order_item(product_id, order_id, amount) values(2, 2, 1);
insert into order_item(product_id, order_id, amount) values(8, 2, 4);
insert into order_item(product_id, order_id, amount) values(4, 3, 7);
insert into order_item(product_id, order_id, amount) values(3, 4, 2);
insert into order_item(product_id, order_id, amount) values(9, 4, 1);
insert into order_item(product_id, order_id, amount) values(10, 4, 1);
insert into order_item(product_id, order_id, amount) values(2, 4, 6);
insert into order_item(product_id, order_id, amount) values(7, 5, 1);
insert into order_item(product_id, order_id, amount) values(3, 5, 2);
insert into order_item(product_id, order_id, amount) values(4, 6, 3);
insert into order_item(product_id, order_id, amount) values(1, 7, 1);
insert into order_item(product_id, order_id, amount) values(8, 7, 5);
insert into order_item(product_id, order_id, amount) values(9, 8, 2);
insert into order_item(product_id, order_id, amount) values(10, 8, 1);
insert into order_item(product_id, order_id, amount) values(7, 8, 1);

commit;

select * from products_out_of_stock;
select * from total_sales;