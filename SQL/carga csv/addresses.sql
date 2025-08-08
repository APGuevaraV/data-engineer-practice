create temporary table addresses_temp(
id int,
direccion varchar(50)
);

create table addresses(
id int,
direccion varchar(50)
);

LOAD DATA infile 'C:/ProgramData/MySQL/MySQL Server 8.4/Uploads/direcciones.csv'
INTO TABLE addresses_temp
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

select * from addresses_temp;

INSERT INTO addresses
SELECT 
	id,
    nullif(
		TRIM(
        REPLACE(
        REPLACE(direccion,CHAR(13),'')
        ,CHAR(10),'')
        )
    ,'')
    from addresses_temp;
select * from addresses;