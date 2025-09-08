--Obtén el nombre de cada cliente y el monto total que ha gastado 
--en todas sus órdenes, ordenado de mayor a menor.
select c.nombre, sum(o.total) as total
from clientes c 
join ordenes o 
on o.cliente_id = c.id
group by c.id
order by total desc;

-- Muestra las categorías de productos junto con el monto total vendido en cada una.