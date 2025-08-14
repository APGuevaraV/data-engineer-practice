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
