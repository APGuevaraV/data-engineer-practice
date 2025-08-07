create temporary table ventas_temp(
id_venta int,
cliente varchar(10),
monto decimal(10,2),
estado_pago varchar(15)
);

create table ventas_estado(
id_venta int,
cliente varchar(10),
monto decimal(10,2),
estado_pago varchar(10),
alerta_pago varchar(15)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.4/Uploads/ventas.csv'
INTO TABLE ventas_temp
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

insert into ventas_estado
	SELECT
		id_venta,
		cliente,
		monto,
		estado_pago,
        CASE
			WHEN TRIM(REPLACE(REPLACE(estado_pago, CHAR(13), ''), CHAR(10), '')) = 'Pendiente' AND monto > 1000 THEN 'Revisar'
            ELSE 'OK'
		END as alerta_pago 
	FROM ventas_temp;

select * from ventas_estado;

