SELECT Año, Mes,Categoria , SUM(Monto) AS Total
FROM Ventas
GROUP BY ROLLUP(Año, Mes,Categoria)
ORDER BY Año, Mes, Categoria;