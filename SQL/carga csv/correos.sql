create temporary table correo_temp(
id int,
correo varchar(50)
);

create table correo(
id int,
correo varchar(50)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.4/Uploads/correos.csv'
INTO table correo_temp
FIELDS terminated by ','
enclosed by '"'
LINES terminated by '\r\n'
ignore 1 rows;
select * from correo_temp;
insert into correo(id,correo)
select
id,
nullif(
trim(
	replace(
		replace(correo,CHAR(13),'')
    ,char(10),'')
    )
,'')
from correo_temp WHERE correo LIKE '%@%';
select * from correo;
