CREATE TEMPORARY TABLE empleados_temp(
    id int,
    nombre varchar(10),
    departamento varchar(20),
    sueldo decimal(10,2)
)

LOAD DATA INFILE 'empleados.csv'
INTO TABLE empleados_temp
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

----
CREATE TABLE empleados(
    id int,
    nombre varchar(10),
    departamento varchar(20),
    sueldo decimal(10,2),
    nivel varchar(10)
);

CREATE TEMPORARY TABLE empleados_tempo(
    id int,
    nombre varchar(10),
    departamento varchar(20),
    sueldo decimal(10,2)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.4/Uploads/empleados.csv'
INTO TABLE  empleados_tempo
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

INSERT INTO empleados (id, nombre, departamento, sueldo, nivel)
SELECT 
    id,
    nombre,
    departamento,
    sueldo,
    CASE 
        WHEN sueldo >= 3500 THEN 'Senior'
        ELSE 'Junior'
    END AS nivel
FROM empleados_temp;
select * from empleados;

-----con fecha actual
INSERT INTO empleados_final (id, nombre, departamento, sueldo, nivel, fecha_carga)
SELECT 
    id,
    nombre,
    departamento,
    sueldo,
    CASE 
        WHEN sueldo >= 3500 THEN 'Senior'
        ELSE 'Junior'
    END,
    CURDATE()
FROM empleados_temp;
