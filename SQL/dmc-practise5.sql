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

select a.MES_CORTE,
		   b.tipo,
		   b.SUBTIPO,
	       sum(im_capital_asegurado)
	  from [dbo].[TB_SEGURO]      a
inner join [dbo].[TB_TIPO_SEGURO] b
        on a.cd_producto = b.codigo
     group by  rollup (a.MES_CORTE,b.tipo,b.SUBTIPO)
	 order by 1,2,3

select a.MES_CORTE,
		   b.tipo,
		   b.SUBTIPO,
	       sum(im_capital_asegurado)
	  from [dbo].[TB_SEGURO]      a
inner join [dbo].[TB_TIPO_SEGURO] b
        on a.cd_producto = b.codigo
     group by  cube (a.MES_CORTE,b.tipo,b.SUBTIPO)
	 order by 1,2,3

select a.MES_CORTE,
		   b.tipo,
		   b.SUBTIPO,
	       sum(im_capital_asegurado)
	  from [dbo].[TB_SEGURO]      a
inner join [dbo].[TB_TIPO_SEGURO] b
        on a.cd_producto = b.codigo
	 group by grouping sets (
							(a.MES_CORTE,b.tipo,b.SUBTIPO),
							(b.tipo),
							()
							)