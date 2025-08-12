select count(*) as cantidad , ifnull(departamento,'Sin Asignar')
from empleados
group by ifnull(departamento,'Sin Asignar')
order by cantidad;

select 
ifnull(year(FechaIngreso),'Sin Asignar') as anio,
round(avg(sueldo),2) as promedio_sueldo
from empleados
group by anio;

select
NombreCompleto,
case
	WHEN timestampdiff(YEAR,FechaIngreso,curdate()) < 2 THEN 'Nuevo'
    WHEN timestampdiff(YEAR,FechaIngreso,curdate()) between 2 and 5 THEN 'Intermedio'
    ELSE 'Veterano'
END
as categoria
from empleados;

with CTE_rangos as(
select 
NombreCompleto,
sueldo,
	CASE
		WHEN Sueldo >=3500 then 'ALTO'
		WHEN Sueldo >=2500 and Sueldo <=3499 then 'MEDIO'
		ELSE 'BAJO'
	END as rango
from empleados
)
select rango,count(*) as cantidad from CTE_rangos group by rango;

SELECT
departamento,
min(FechaIngreso) as contratacion_antigua,
max(FechaIngreso) as contratacion_reciente
from empleados
group by departamento;