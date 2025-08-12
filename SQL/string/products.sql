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