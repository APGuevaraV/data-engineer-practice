select 
id ,
    cliente,
    producto,
    categoria ,
    fecha ,
    cantidad ,
    total,
	row_number() over (order by fecha) AS fila
 from ventas;