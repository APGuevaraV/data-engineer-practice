-- Obtén el promedio de notas por curso y ordénalos de mayor a menor.
select c.nombre as curso,avg(i.nota) as promedio from 
inscripciones i 
join cursos c 
on i.curso_id = c.id
group by i.curso_id
order by promedio desc;


-- Muestra los nombres de los estudiantes junto con los cursos que llevan, 
-- pero solo aquellos de la ciudad Lima.

select e.nombre, c.nombre from 
estudiantes e 
join inscripciones i 
on e.id = i.estudiante_id
join cursos c 
on i.curso_id = c.id
where e.ciudad = 'Lima';


-- Lista el curso con la nota más alta de cada estudiante 
-- (usa JOIN y subconsulta o función de ventana).

with cte_NotaPorEstudiante as (
select e.nombre as estudiante, c.nombre as curso, i.nota from 
inscripciones i
join estudiantes e
on i.estudiante_id = e.id
join cursos c 
on c.id = i.curso_id
),cte_MaxNota AS (
    SELECT estudiante, 
           curso, 
           nota,
           ROW_NUMBER() OVER (PARTITION BY estudiante ORDER BY nota DESC) AS rn
    FROM cte_NotaPorEstudiante
)
SELECT estudiante, curso, nota
FROM cte_MaxNota
WHERE rn = 1;


-- Muestra el número de estudiantes inscritos por categoría de curso.

select c.categoria, count(distinct e.nombre ) cantidad_alumnos from
estudiantes e 
join inscripciones i 
on i.estudiante_id = e.id
join cursos c
on c.id = i.curso_id
group by categoria;


select e.nombre,count(c.nombre) as nro from 
inscripciones i
join estudiantes e 
on i.estudiante_id = e.id
join cursos c
on c.id = i.curso_id
where c.categoria = 'Tecnología'
group by e.nombre
having COUNT(c.id) > 1;


-- Obtén el total gastado por cada cliente, mostrando el nombre del cliente y 
-- el monto total, ordenado de mayor a menor.

select c.nombre, sum(o.total) as total from 
clientes c 
join ordenes o 
on c.id = o.cliente_id
group by c.nombre
order by total desc;

-- Lista las categorías de productos junto con el monto total vendido en cada una.
select p.categoria, sum(deto.cantidad * deto.precio_unitario) as total
from productos p
join detalle_orden deto
on p.id = deto.producto_id
group by p.categoria
order by total desc;


-- Muestra el producto más vendido en cantidad de unidades (no en dinero).
select p.nombre , sum(deto.cantidad) as cantidad
from productos p
join detalle_orden deto
on deto.producto_id = p.id
group by p.nombre
order by cantidad desc limit 1;