create temporary table telefonos_temp(
id int,
telefono varchar(20)
);

create table telefonos(
id int,
telefono varchar(20)
);

LOAD DATA infile 'C:/ProgramData/MySQL/MySQL Server 8.4/Uploads/telefonos.csv'
INTO TABLE telefonos_temp
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

select * from telefonos_temp;
insert into telefonos(id,telefono)
select
id,
NULLIF(
    TRIM(
        REPLACE(
            REPLACE(
                REPLACE(
                    REPLACE(
                        REPLACE(telefono, '(', ''), 
                        ')', ''
                    ),
                    '-', ''
                ),
                ' ', ''
            ),
            '+', ''
        )
    ),
    ''
)
from telefonos_temp;

select * from telefonos;