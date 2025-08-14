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
select c.nombre 
from clientes c
where (
    select max(monto)
    from pedidos pedido
    where p.id_cliente = c.id_cliente) 
    > any(
    select precio 
    from productos 
    where categoria = 'Accesorios'
    );


--Encontrar los clientes cuyo monto de todos sus pedidos sea
-- mayor que el precio más alto de la categoría Muebles.
select distinct c.nombre 
from clientes c
where(
    SELECT MIN(monto)
    FROM pedidos p
    WHERE p.id_cliente = c.id_cliente
) > 
    all(
    select (precio) 
    from productos
     where categoria = 'Muebles');

--Mostrar los clientes que tengan al menos un pedido con monto
-- mayor al promedio de todos los pedidos.
select c.nombre from clientes c 
where exists(
			select 1 from pedidos p
			where p.id_cliente = c.id_cliente
            and p.monto > (
                select avg(p.monto)
                from pedidos
                )
            )



SELECT DISTINCT c.nombre
FROM clientes c
WHERE EXISTS (
    SELECT 1
    FROM pedidos p
    WHERE p.id_cliente = c.id_cliente
      AND p.monto > ALL (
          SELECT p2.monto
          FROM pedidos p2
          JOIN clientes c2 ON p2.id_cliente = c2.id_cliente
          WHERE c2.ciudad = c.ciudad
            AND p2.monto > 1000
      )
);


--Listar los nombres de empleados que estén asignados a proyectos
-- cuyo presupuesto sea mayor a 5000.
select e.nombre
from empleados e 
where e.id_empleado in(
	select a.id_empleado 
	from asignaciones a
	where a.id_proyecto in (
		select p.id_proyecto from proyectos p
		where p.presupuesto > 5000) 
						);

--Obtener empleados cuyo sueldo sea mayor que cualquier presupuesto
-- de proyectos con nombre que contenga la palabra App.

select e.nombre, e.sueldo
from empleados e
where e.sueldo > any(
	select p.presupuesto 
    from proyectos p
	where p.nombre_proyecto like '%App%'
);

--Listar empleados cuyo sueldo sea mayor que todos los presupuestos 
--de proyectos asignados a Marketing.
select e.nombre, e.sueldo
from empleados e
where e.sueldo > all(
	select p.presupuesto 
    from proyectos p
	join asignaciones a on p.id_proyecto = a.id_empleado
    join empleados em on em.id_empleado = a.id_empleado
    where em.departamento = 'Marketing'
);

--Mostrar los empleados que estén asignados a al menos un proyecto
-- con más de 80 horas trabajadas.
select e.nombre
from empleados e
where exists(
	select 1 from asignaciones a
	where a.id_empleado = e.id_empleado
	and a.horas > 80
);