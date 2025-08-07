--limpieza y carga

create temporary table temp_empleados(
id_empleado int,
nombre varchar(15),
cargo varchar(15),
sueldo decimal(10,2),
departamento varchar(15)
);

create table empleados_real(
id_empleado int,
nombre varchar(15),
cargo varchar(15),
sueldo decimal(10,2),
departamento varchar(15)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.4/Uploads/empleados3.csv'
into table temp_empleados
FIELDS TERMINATED BY ','
enclosed by '"'
LINES terminated by '\r\n'
ignore 1 rows;

INSERT INTO empleados_real
SELECT 
    id_empleado,
    NULLIF(TRIM(REPLACE(REPLACE(nombre, CHAR(13), ''), CHAR(10), '')), '') AS nombre,
    NULLIF(TRIM(REPLACE(REPLACE(cargo, CHAR(13), ''), CHAR(10), '')), '') AS cargo,
    sueldo,
    NULLIF(TRIM(REPLACE(REPLACE(departamento, CHAR(13), ''), CHAR(10), '')), '') AS departamento
FROM temp_empleados;
