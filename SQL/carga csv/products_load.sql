create temporary table productos_temp(
id int,
nombre varchar(15),
categoria varchar(15),
precio decimal(10,2)
);

create table productos_clasificados(
id int,
nombre varchar(15),
categoria varchar(15),
precio decimal(10,2),
rango_precio varchar(7)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.4/Uploads/productos.csv'
INTO TABLE productos_temp
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

INSERT INTO productos_clasificados
SELECT 
	id ,
	nombre ,
	categoria ,
	precio ,
    CASE
		WHEN precio > 2000 THEN 'ALTO'
        WHEN precio >=1000 and precio <=2000 THEN 'MEDIO'
        ELSE 'BAJO'
	END	as rango_precio
FROM productos_temp;
select * from productos_clasificados;
