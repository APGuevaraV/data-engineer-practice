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


(select c.nombre
from clientes c 
join ventas v 
on c.id_cliente=v.id_cliente
group by c.id_cliente)
union all
(
select c.nombre from clientes c
left join ventas v 
on c.id_cliente=v.id_cliente
where v.id_venta is null
); 

select nombre_producto
from productos p 
inner join ventas v
on p.id_producto = v.id_producto
group by p.id_producto,nombre_producto
having count(v.id_venta)>1;

select distinct clientes_union.nombre
from
(
select c.id_cliente,c.nombre
from clientes c 
join ventas v on c.id_cliente=v.id_cliente
where v.id_producto=104
union
select c.id_cliente,c.nombre
from clientes c 
join ventas v on c.id_cliente=v.id_cliente
where v.id_producto=103
) as clientes_union
left join ventas v2
on clientes_union.id_cliente = v2.id_cliente
and v2.id_producto=101
where v2.id_venta is null;

select c.nombre 
from clientes c 
join ventas v
on c.id_cliente=v.id_cliente
group by c.id_cliente
having count(v.id_venta) = 1;

