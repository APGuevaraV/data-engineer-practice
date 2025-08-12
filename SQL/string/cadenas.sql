--Muestra el primer nombre y primer apellido en columnas separadas,
-- reemplazando cualquier letra "í" por "i" en el nombre.

select 
substring_index(replace(NombreCompleto,'í','i'),' ',1) as nombre,
substring_index(replace(NombreCompleto,'í','i'),' ',-1) as apellido
from empleados;

--Crea una columna calculada que muestre cuántos días lleva el empleado en la empresa.
--Además, calcula la fecha en que cumplirá 3 años desde su ingreso.
select 
datediff(current_Date(),FechaIngreso) as días_en_empresa,
date_add(FechaIngreso, INTERVAL 3 YEAR)
from empleados;


--Muestra el sueldo total de cada empleado sumando sueldo y comisión, 
--usando ISNULL para que los NULL se consideren 0.
select Sueldo + IFNULL(Comision,0) as total from empleados;

--Crea una columna llamada BonoExtra que sea:
select if(Comision >500,'Sí','No') as bono_extra from empleados;

--Crea una consulta que muestre el porcentaje de comisión sobre el sueldo (Comision / Sueldo)
select round((comision/nullif(sueldo,0))*100,2 )
as porcentaje_comision 
from empleados;

select upper(NombreCompleto) as nombre,
	length(NombreCompleto) as longitud
 from empleados;

select 
date_format(FechaIngreso,'%d/%m/%Y') as fecha,
date_format(FechaIngreso,'%W') as dia_semana
from empleados;

select concat('Empleado:',NombreCompleto,' - ','Departamento:',IFNULL(departamento,'Sin Asignar')) as nombre
from empleados;

select
sueldo,
case
	WHEN sueldo >= 3000 THEN 'Alto'
    When sueldo >=2500 and sueldo <3000 THEN 'Medio'
    else 'Bajo'
END
as NivelSueldo
from empleados;

select
NombreCompleto,
IF(FechaIngreso, TIMESTAMPDIFF(YEAR, FechaIngreso, CURDATE()), 'Sin Registro') AS anios_empresa
from empleados;

select ifnull(Departamento,'Sin Departamento') as depto,
count(*) as nro_empleados
from empleados
GROUP BY IFNULL(Departamento,'Sin Departamento');

select 
round(avg(sueldo),2) as promedio,
IFNULL(Departamento,'Sin Departamento') AS departamento
from empleados
group by IFNULL(Departamento,'Sin Departamento')  order by promedio desc;


select departamento,
avg(timestampdiff(year,FechaIngreso,CURDATE())) as promedio_anios
from empleados
where FechaIngreso is not null
group by departamento; 

with cte_rangos as (
select 
	CASE
		WHEN sueldo >=3000 THEN 'ALTO'
		WHEN SUELDO >=2500 AND SUELDO <3000 THEN 'MEDIO'
		ELSE 'BAJO'
	END
as nivel_sueldo,
ifnull(comision,0) as comision
from empleados
)
select sum(comision),nivel_sueldo
from cte_rangos
group by nivel_sueldo;

select 
departamento,
min(FechaIngreso) as mas_antiguo,
max(FechaIngreso) as mas_reciente
from empleados
WHERE FechaIngreso IS NOT NULL
group by departamento;


select substring_index(cliente,' ',1) as nombre,
upper(categoria) as categoria
from ventas;

select producto,
(precio * cantidad)-ifnull(descuento,0) as total_venta
from ventas;

select 
categoria,
sum(cantidad) as cantidad_total,
round(avg(precio),2) as promedio_precio,
sum(precio*cantidad) as tota_ventas
from ventas
group by categoria;

select 
CASE 
        WHEN MONTH(FechaVenta) BETWEEN 1 AND 6 THEN 1
        ELSE 2
    END AS semestre,
	ROUND(SUM(Precio * Cantidad), 2) AS total_ventas
from ventas
where year(FechaVenta)=2024
group by semestre
order by semestre;

select
vendedor,
min(FechaVenta) as primera_venta,
max(FechaVenta) as ultima_venta
from ventas
group by vendedor;