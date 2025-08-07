create temporary table employees_temp(
id int,
nombre varchar(15),
departamento varchar(15),
sueldo decimal(10,2)
);

create table empleados_final(
id int,
nombre varchar(15),
departamento varchar(15),
sueldo decimal(10,2),
nivel varchar(10)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.4/Uploads/empleados2.csv'
INTO table employees_temp
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 rows;

INSERT INTO empleados_final
SELECT 
	id ,
	nombre,
	departamento ,
	sueldo,
	CASE
		WHEN sueldo >=3500 THEN 'Senior'
        ELSE 'Junior'
	END as nivel
FROM employees_temp;

select * from empleados_final;

