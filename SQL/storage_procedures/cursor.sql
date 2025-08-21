delimiter //
create procedure registrar_logs()
begin
	declare done int default false;
    declare v_nombre varchar(50);
    declare v_salario decimal(10,2);
    declare v_id int;
    
    declare CUR CURSOR FOR SELECT id,nombre,salario from empleados;
    declare continue handler for NOT FOUND SET done = True;
    open CUR;
    read_loop: LOOP
		fetch CUR into v_id, v_nombre,v_salario;
        if done THEN
			LEAVE read_loop;
		end if;
        
		insert into logs_proceso(descripcion)values(
        concat('Empleado ',v_nombre,'tiene salario ',v_salario));
        
	end loop;
    close CUR;
end
//
delimiter ;


call registrar_logs();
select * from logs_proceso;