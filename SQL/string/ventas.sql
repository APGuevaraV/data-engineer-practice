select count(*) as cantidad , ifnull(departamento,'Sin Asignar')
from empleados
group by ifnull(departamento,'Sin Asignar')
order by cantidad;

select 
ifnull(year(FechaIngreso),'Sin Asignar') as anio,
round(avg(sueldo),2) as promedio_sueldo
from empleados
group by anio;