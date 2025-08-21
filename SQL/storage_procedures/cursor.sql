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


delimiter //
create procedure insertar_categorias()
begin
	declare v_categoria varchar(20);
    declare v_salario varchar(20);
    declare v_nombre varchar(50);
    declare v_id int;
    declare done int default false;
    
    DECLARE CUR cursor for select id,nombre,salario from empleados2;
    declare continue handler for not found set done = True;
    open CUR;
    read_loop: LOOP
		fetch CUR into v_id,v_nombre,v_salario;
        if done  then
			leave read_loop;
		end if;
        set v_categoria = case
        when v_salario < 1000 THEN 'Bajo'
        when v_salario >=1000 and v_salario <=1500 then 'Medio'
        when v_salario >1500 then 'Alto'
        end;
        insert into categorias(nombre,categoria)values(v_nombre,v_categoria);
	end loop;
    close CUR;
end
//
delimiter ;

drop procedure if exists insertar_categorias;

call insertar_categorias();
select * from categorias;