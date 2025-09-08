--Obtén el nombre de cada cliente y el monto total que ha gastado 
--en todas sus órdenes, ordenado de mayor a menor.
select c.nombre, sum(o.total) as total
from clientes c 
join ordenes o 
on o.cliente_id = c.id
group by c.id
order by total desc;

-- Muestra las categorías de productos junto con el monto total vendido en cada una.
select p.categoria, sum(p.precio * deto.cantidad) 
from productos p
join detalleorden deto
on deto.producto_id = p.id
group by p.categoria

--Encuentra los clientes que han comprado más de un producto distinto en una misma orden.
select c.id,c.nombre, count(distinct(deto.producto_id)) as nro 
from clientes c
join ordenes o 
on c.id = o.cliente_id
join detalleorden deto
on deto.orden_id = o.id
group by c.id
having nro > 1;