select 
upper(nombre),
upper(categoria),
round(precio,2) from productos order by precio desc;

select 
nombre,
date_format(fecha_ingreso,'%d-%m-%Y') as fecha_ingreso,
date_format(fecha_ingreso,'%W') as dia_ingreso
from productos;

select 
concat('Producto: ',nombre,' - ','Categoría: ', categoria) as categoria
from
productos;


select 
precio,
case
		when precio >= 3000 then 'Alto'
        when precio between 1000 and 2999.99 then 'Medio'
        else 'Bajo'
end as categoria
from productos;

select 
ifnull(fecha_ingreso,'Sin Asignar') as fecha,
CASE
        WHEN fecha_ingreso IS NULL THEN 'Sin Asignar'
        ELSE TIMESTAMPDIFF(MONTH, fecha_ingreso, CURDATE())
    END AS meses
from productos;


select 
departamento,
avg(sueldo) as sueldo_promedio
from empleados
group by departamento 
order by sueldo_promedio desc;

with CTE_promedio as(
select departamento,avg(ventas) as promedio from empleados group by departamento
)
select 
e.departamento,
e.nombre,
e.ventas
from empleados e
join CTE_promedio c
on e.departamento=c.departamento
where e.ventas > c.promedio;

with cte_categoria as
(
select 
 sueldo,
 CASE
	when sueldo >=5000 then 'alto'
    when sueldo between 3000 and 4999.99 then 'medio'
    else 'bajo'
 END as categoria
 from empleados
)
select categoria, sueldo from cte_categoria
order by categoria,sueldo desc;