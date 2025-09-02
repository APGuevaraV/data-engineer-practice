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