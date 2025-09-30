--Muestra el nombre de cada empleado y el total en dinero que generó en ventas.
SELECT e.empleado_id,e.nombre, SUM(p.precio*v.cantidad) as total
FROM Empleados e
JOIN Ventas v
ON e.empleado_id = v.empleado_id
JOIN Productos p
ON v.producto_id = p.producto_id
group by e.nombre,e.empleado_id
order by total desc;


--Lista el nombre, el departamento y el salario del empleado que más gana en cada departamento.
SELECT nombre,departamento,salario
FROM(
SELECT nombre, departamento, salario,
RANK() OVER(PARTITION BY departamento ORDER BY salario DESC) AS ranking
from Empleados
) t
where t.ranking = 1;

SELECT e.nombre, e.departamento, e.salario
FROM Empleados e
WHERE e.salario = (
    SELECT MAX(salario)
    FROM Empleados
    WHERE departamento = e.departamento
);