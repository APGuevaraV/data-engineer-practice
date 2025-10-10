SELECT Año, Mes,Categoria , SUM(Monto) AS Total
FROM Ventas
GROUP BY ROLLUP(Año, Mes,Categoria)
ORDER BY Año, Mes, Categoria;

SELECT Año, Mes, Categoria, SUM(Monto) AS Total
FROM Ventas
GROUP BY CUBE(Año, Mes, Categoria)
ORDER BY Año, Mes, Categoria;

SELECT grouping_id(Año, Mes, Categoria),
	   Año, Mes, Categoria, SUM(Monto) AS Total
FROM Ventas
GROUP BY GROUPING SETS (
    --(Año, Mes, Categoria), -- detalle completo
    (Año, Mes),            -- subtotal mes
    (Año, Categoria),      -- subtotal categoría por año
    (Año),                 -- total año
    (Mes, Categoria),                     -- total general
	(Mes),
	(Categoria),
	()
)
ORDER BY 1