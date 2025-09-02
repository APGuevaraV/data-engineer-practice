-- Obtén el promedio de notas por curso y ordénalos de mayor a menor.
select c.nombre as curso,avg(i.nota) as promedio from 
inscripciones i 
join cursos c 
on i.curso_id = c.id
group by i.curso_id
order by promedio;