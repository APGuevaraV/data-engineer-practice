--Muestra el nombre de cada empleado y el total en dinero que generó en ventas.
SELECT e.empleado_id,e.nombre, SUM(p.precio*v.cantidad) as total
FROM Empleados e
JOIN Ventas v
ON e.empleado_id = v.empleado_id
JOIN Productos p
ON v.producto_id = p.producto_id
group by e.nombre,e.empleado_id
order by total desc;