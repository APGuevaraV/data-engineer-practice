--in & out -condicional
delimiter //
create procedure verificar_aumento(
in p_id int,
out p_mensaje varchar(100)
)
begin
	declare v_salario decimal(10,2);
    select salario into v_salario from empleados where id=p_id;
    if v_salario < 1000 THEN
		set p_mensaje = 'Empleado califica para aumento';
	else 
		set p_mensaje = 'El empleado NO califica para aumento';
    end if;
end;
//
delimiter ;

drop procedure if exists verificar_aumento;

call verificar_aumento(2,@mensaje);
select @mensaje;

DELIMITER //
CREATE PROCEDURE calcular_aumentos()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE v_id INT;
    DECLARE v_salario DECIMAL(10,2);
    DECLARE v_area VARCHAR(30);
    DECLARE v_nuevo DECIMAL(10,2);

    DECLARE cur CURSOR FOR SELECT id, salario, area FROM empleados;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO v_id, v_salario, v_area;
        IF done THEN
            LEAVE read_loop;
        END IF;

        SET v_nuevo = CASE 
            WHEN v_area = 'IT' THEN v_salario * 1.10
            WHEN v_area = 'Ventas' THEN v_salario * 1.05
            WHEN v_area = 'RRHH' THEN v_salario * 1.07
            ELSE v_salario
        END;

        INSERT INTO aumentos (id_empleado, nuevo_salario)
        VALUES (v_id, v_nuevo);
    END LOOP;

    CLOSE cur;

    INSERT INTO logs_proceso (descripcion) VALUES ('Cálculo de aumentos realizado');
END;
//
DELIMITER ;
CALL calcular_aumentos();
SELECT * FROM aumentos;
SELECT * FROM logs_proceso;
