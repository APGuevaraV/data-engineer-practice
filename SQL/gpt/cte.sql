/*
selecciona los nombres de los empleados 
cuyo salario sea mayor a 4000.
*/

with CTE_salary
as (
select * from empleados where salario > 4000
	)
select * from CTE_salary;


/*
Crea una CTE que una las tablas empleados y departamentos. 
Luego, lista el nombre del empleado, su departamento y su 
salario.
*/

with CTE_total_employees
as (
select empleados.nombre as empleado , departamentos.nombre as departamento, empleados.salario
from empleados 
join departamentos 
on empleados.departamento_id = departamentos.id
	)
select * from CTE_total_employees;

/*
Crea una CTE que ordene a los empleados por salario de 
mayor a menor y selecciona solo a los 3 con mayor salario.


*/

with CTE_employees_ordered
as (
select * from empleados order by salario desc
)

select nombre,salario from CTE_employees_ordered limit 3;

/*
Primero, crea una CTE que calcule el salario promedio de 
todos los empleados. Luego, usando otra CTE, lista los nombres
de los empleados que ganan más que ese salario promedio.
*/

with CTE_promedio
as (
select avg(salario) as promedio 
from empleados
), CTE_empleados
as (
select nombre,salario from CTE_promedio,empleados
where salario > CTE_promedio.promedio
)

select * from CTE_empleados;