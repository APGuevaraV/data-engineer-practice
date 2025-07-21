CREATE TABLE CUSTOMERS(
customer_id int auto_increment primary key,
name varchar(50) not null
);

CREATE TABLE ORDERS(
order_id int auto_increment primary key,
customer_id int not null,
total float,
FOREIGN KEY(customer_id) REFERENCES CUSTOMERS(customer_id)
);

INSERT INTO customers (name) VALUES
('Ana Gómez'),
('Luis Pérez'),
('Carlos Ruiz'),
('María Torres'),
('Lucía Fernández'),
('Pedro Rojas'),
('Sofía Vargas'),
('Miguel Ramírez'),
('Valeria Castro'),
('José Herrera'),
('Daniela Mendoza'),
('Andrés Navarro'),
('Paula Díaz'),
('Jorge León'),
('Carmen Paredes'),
('Rodrigo Salas'),
('Esteban Flores'),
('Isabel Silva'),
('Gabriel Campos'),
('Fernanda Soto');

INSERT INTO orders (order_id, customer_id, total) VALUES
(1001, 1, 150.00),
(1002, 2, 200.50),
(1003, 3, 300.00),
(1004, 4, 99.99),
(1005, 5, 450.75),
(1006, 6, 120.00),
(1007, 7, 80.00),
(1008, 8, 215.20),
(1009, 9, 178.60),
(1010, 10, 310.10),
(1011, 11, 140.40),
(1012, 12, 199.99),
(1013, 13, 275.00),
(1014, 14, 500.00),
(1015, 15, 230.00),
(1016, 16, 95.75),
(1017, 17, 135.35),
(1018, 18, 410.00),
(1019, 19, 220.00),
(1020, 20, 165.80),
(1021, 3, 89.90),
(1022, 7, 150.00),
(1023, 1, 200.00),
(1024, 5, 175.50),
(1025, 10, 330.00),
(1026, 15, 120.75),
(1027, 18, 215.00),
(1028, 2, 450.00),
(1029, 8, 99.99),
(1030, 13, 310.20);

select COUNT(total) as total_ordenes ,customers.name from orders 
inner join customers on orders.customer_id = customers.customer_id 
group by customers.customer_id order by  total_ordenes desc;

select SUM(total) as total_gastado ,customers.name from orders 
inner join customers on orders.customer_id = customers.customer_id 
group by customers.customer_id order by  total_gastado desc;

select * from customers left join orders
on customers.customer_id = orders.customer_id
where orders.order_id is null;