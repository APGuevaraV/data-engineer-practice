select c.nombre
from clientes c
where c.id_cliente in (
select p.id_cliente from pedidos p
where year(p.fecha) = 2025 and month(p.fecha) = 3
);

select c.nombre
from clientes c
where ( select 
		max(monto) from pedidos p
        where p.id_cliente = c.id_cliente
        ) > any(
        select precio from productos
        where categoria = 'Muebles'
        );

select c.nombre 
from clientes c 
where (
select min(monto) from pedidos p
where c.id_cliente = p.id_cliente
) > all(select precio from productos
where categoria = 'Accesorios');

select c.nombre 
from clientes c
where 
 exists (
	select 1 
    from pedidos p 
    where c.id_cliente =p.id_cliente
    and p.monto > (
    select avg(p2.monto) 
    from pedidos p2
    join clientes c2 on c2.id_cliente = p2.id_cliente
    where c2.ciudad = c.ciudad)
);


select c.nombre,c.ciudad
from clientes c
where exists (
	select 1 from pedidos p 
    where p.id_cliente = c.id_cliente
   and p.monto > (select  avg(p.monto) from pedidos) 
);


