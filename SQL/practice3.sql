(select distinct c.nombre
from clientes c
join ventas v on c.id_cliente=v.id_cliente
where v.id_producto=101)
union
(select distinct c.nombre
from clientes c
join ventas v on c.id_cliente=v.id_cliente
where v.id_producto=103);

select c.nombre from clientes c 
join ventas v 
on c.id_cliente = v.id_cliente
where v.id_producto = 101
INTERSECT
select c.nombre from clientes c 
join ventas v 
on c.id_cliente = v.id_cliente
where v.id_producto = 103;

select c.nombre from clientes c 
LEFT JOIN  ventas v 
on c.id_cliente = v.id_cliente;

--except
SELECT DISTINCT c.nombre
FROM Clientes c
JOIN Ventas v ON c.id_cliente = v.id_cliente
WHERE v.id_producto = 102  

EXCEPT

SELECT DISTINCT c.nombre
FROM Clientes c
JOIN Ventas v ON c.id_cliente = v.id_cliente
WHERE v.id_producto = 101; 

--except
SELECT p.id_producto
FROM Producto p 

EXCEPT

SELECT p.id_producto
FROM Producto p
JOIN Ventas v ON p.id_producto = v.id_producto
