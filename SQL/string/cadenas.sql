--Muestra el primer nombre y primer apellido en columnas separadas,
-- reemplazando cualquier letra "í" por "i" en el nombre.

select 
substring_index(replace(NombreCompleto,'í','i'),' ',1) as nombre,
substring_index(replace(NombreCompleto,'í','i'),' ',-1) as apellido
from empleados;

select 
datediff(current_Date(),FechaIngreso) as días_en_empresa,
date_add(FechaIngreso, INTERVAL 3 YEAR)
from empleados;