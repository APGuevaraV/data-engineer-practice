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

(select nombre_producto
from productos p 
left join ventas v
on p.id_producto = v.id_producto
where v.id_venta is null)
union
(select nombre_producto
from productos p 
join ventas v
on p.id_producto = v.id_producto
group by p.id_producto, nombre_producto
having count(v.id_venta) =1
);

-- union
(
select c.nombre
from clientes c
join ventas v
on c.id_cliente = v.id_cliente
)
union
(select c2.nombre
from clientes c2
where left(c2.nombre,1)='L');

select v.id_producto,p.nombre_producto
from ventas v
join productos p 
on v.id_producto=p.id_producto
group by p.id_producto,p.nombre_producto
having count(distinct(v.id_cliente)) >1;

-- except
select distinct clientes_audifonos.nombre
from
(select c.id_cliente,c.nombre
from clientes c 
join ventas v on c.id_cliente=v.id_cliente
where v.id_producto=104) as clientes_audifonos
left join ventas v2
on clientes_audifonos.id_cliente = v2.id_cliente
and v2.id_producto=103
where v2.id_venta is null;

--Lista de productos que nunca han sido vendidos o que fueron comprados solo por un cliente distinto.

(select v.id_producto,p.nombre_producto
from productos p 
left join ventas v 
on p.id_producto = v.id_producto
where v.id_venta is null)
union
(
select v2.id_producto,p2.nombre_producto
from productos p2 
join ventas v2 
on p2.id_producto = v2.id_producto
group by v2.id_producto,p2.nombre_producto
having count(v2.id_cliente) = 1
)

--Clientes que compraron Laptop y Celular, pero no Tablet.
select distinct laptop_tablets.nombre from 
(
		(
        select c.id_cliente,c.nombre
		from clientes c 
		join ventas v on c.id_cliente = v.id_cliente
		where v.id_producto=101
        and c.id_cliente in(
        select v2.id_cliente
		from ventas v2
		where v2.id_producto=102)
        )
) as laptop_tablets
	left join ventas v3
	on v3.id_cliente = laptop_tablets.id_cliente
	and v3.id_producto = 103
	where v3.id_venta is null;