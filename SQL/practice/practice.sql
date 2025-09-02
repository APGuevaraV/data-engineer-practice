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
           ROW_NUMBER() OVER (PARTITION BY curso ORDER BY nota DESC) AS rn
    FROM cte_NotaPorEstudiante
)
SELECT estudiante, curso, nota
FROM cte_MaxNota
WHERE rn = 1;


-- Muestra el número de estudiantes inscritos por categoría de curso.

select c.categoria, count(e.nombre) cantidad_alumnos from
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
having nro >1;