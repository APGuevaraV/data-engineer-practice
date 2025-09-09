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
select p.nombre, sum(deto.cantidad) as nro, sum(deto.cantidad * p.precio) as total_vendido
from productos p 
join detalleorden deto 
on p.id = deto.producto_id
group by p.nombre
order by nro desc limit 1


-- Lista los clientes y la cantidad de órdenes realizadas en el año 2024,
-- mostrando solo a los que tengan más de 1 orden.

SELECT c.nombre, count(o.id) as nro_ordenes
from clientes c 
join ordenes o 
on c.id=o.cliente_id
where year(o.fecha) = 2024
group by c.nombre
having nro_ordenes > 1;


-- Obtén el producto más vendido (por cantidad total) y la cantidad total vendida.
select p.nombre, sum(deto.cantidad) as nro, sum(deto.cantidad * p.precio) as total_vendido
from productos p 
join detalleorden deto 
on p.id = deto.producto_id
group by p.nombre
order by nro desc limit 1
