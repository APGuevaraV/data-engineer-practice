--Listar los nombres de clientes que hayan
-- realizado pedidos en febrero 2025.

select c.nombre
from clientes c 
where c.id_cliente in(
select distinct p.id_cliente
from pedidos p
where month(p.fecha)=2 
and year(p.fecha)=2025
);

--Obtener los clientes cuyo monto más alto de pedido sea mayor
-- que cualquier precio de productos de la categoría Accesorios.
select distinct c.nombre 
from clientes c
join pedidos p
on c.id_cliente = p.id_cliente
where monto > any(select precio from productos where categoria = 'Accesorios');