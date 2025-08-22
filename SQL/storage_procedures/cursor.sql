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



--insert con while

delimiter //
create procedure numeros_almacenados()
begin
	declare contador int default 1;
    while contador <=10 DO
		insert into numeros(valor) values(contador);
        set contador = contador+1;
	end while;
end
//
delimiter ;
call numeros_almacenados();
select * from numeros;

--cursor con case 
delimiter //
create procedure increment_salary()
begin
	declare done int default False;
	declare v_id int;
    declare v_nombre varchar(50);
    declare v_salario decimal(10,2);
    declare v_nuevo_salario decimal(10,2);
    
    declare CUR cursor for select id,nombre,salario from empleados3;
    declare continue handler for not found set done= True;
    open cur;
    read_loop: LOOP
				FETCH CUR into v_id,v_nombre,v_salario;
                if done then
					leave read_loop;
				end if;
                set v_nuevo_salario = case
									when v_salario < 1000 then v_salario*1.20
									when v_salario <=1000 and v_salario <=1500 then v_salario*1.10
									else v_salario*1.05
									end;
				insert into aumentos(id_empleado,nuevo_salario)
                values(v_id,v_nuevo_salario);
	end loop;
    close cur;

end
//
delimiter ; 
call increment_salary();
select * from aumentos;


--while simulando etl
delimiter //
create procedure procesar()
begin
	declare v_id int default 1;
    declare total int;
    select count(*) into total from empleados4;
    while v_id <=total DO
		insert into logs_etl(mensaje)
        values(concat('Procesado empleado con ID:',v_id));
        set v_id = v_id+1;
    end while;
    insert into logs_etl(mensaje)
        values(concat('ETL completado'));
end
//
delimiter ;
drop procedure if exists procesar;
call procesar();
select * from logs_etl;


--acumulador :suma_total con CURSOR
delimiter //
create procedure total_salarios()
begin
	declare done int default False;
    declare v_id INT;
    declare v_nombre VARCHAR(50);
    declare v_salario DECIMAL(10,2);
    declare suma_total decimal(10,2) default 0;
    
    declare CUR cursor for select id,nombre,salario from empleados6;
    declare continue handler for not found set done = True;
    open CUR;
    read_loop: LOOP
		fetch CUR into v_id,v_nombre,v_salario;
        if done then
			leave read_loop;
		end if;
        set suma_total =suma_total +v_salario;
	end loop;
    insert into resumen(total_salarios) values(suma_total);
    close cur;
end 
//
delimiter ;

call total_salarios();
select * from resumen;

--clasificacion con cursor
delimiter //
create procedure clasificacion()
begin
	declare done int default False;
	declare v_id INT;
    declare v_nombre VARCHAR(50);
    declare v_edad INT;
    declare v_categoria varchar(20);
    declare cur cursor for select id,nombre,edad from clientes;
    declare continue handler for not found set done = True;
    open cur;
    read_loop:Loop
		fetch cur into v_id,v_nombre,v_edad;
        if done then
			leave read_loop;
		end if;
        set v_categoria = case
						when v_edad < 18 then 'Menor'
						when v_edad >=18 and v_edad <=59 then 'Adulto'
						else 'Senior'
						end;
		insert into clientes_categoria(nombre,categoria)values(v_nombre,v_categoria);
        end loop;
        close cur;
end
// 
delimiter ;

call clasificacion();
select* from clientes_categoria;

--tabla 5 con while
delimiter //
create procedure multiply_5()
begin
	declare contador int default 1;
    while contador <=10 DO
		insert into tabla_multiplicar(operacion,resultado)
        values(
        concat(contador,'x5'),
        contador*5);
        set contador = contador+1;
	end while;
end
//
delimiter ;

call multiply_5();
select * from tabla_multiplicar;


--aplicar descuento con cursos y case
delimiter //
create procedure descuentos()
begin
	declare v_id int;
    declare v_cliente varchar(50);
    declare v_monto decimal(10,2);
    declare done int default False;
    declare descuento decimal(10,2);
    
    declare CUR cursor for select id,cliente,monto from ventas;
    declare continue handler for not found set done = True;
    
    open cur;
    read_loop: loop
		fetch cur into v_id,v_cliente,v_monto;
        if done then
			leave read_loop;
		end if;
		set descuento = case
						when v_monto <100 then v_monto - v_monto*0.05
						when v_monto >=100 and v_monto <=500 then v_monto - v_monto*0.10
						else v_monto - v_monto*0.15
						end;
		insert into ventas_descuento(cliente,monto_original,monto_con_descuento)
        values( v_cliente,v_monto,descuento );
	end loop;
    close cur;    
end
//
delimiter ;

call descuentos();
select * from ventas_descuento ;

--pago de deuda  con while
delimiter //
create procedure saldo()
begin
	declare mes int default 1;
    declare deuda decimal(10,2);
    set deuda = 2000;
    while deuda <>0 DO
		set deuda = deuda-200;
        insert into pagos(mes,saldo_restante)values
        (mes,deuda);
        set mes = mes+1;
    end while;
end
//
delimiter ;

call saldo();
select * from pagos;

--in out
delimiter //
create procedure bono(in i_id int,out nuevo_salario decimal(10,2))
begin
	declare v_salario decimal(10,2);
    declare v_departamento varchar(50);
    declare bono decimal(10,2);
    
    select salario,departamento into v_salario,v_departamento from empleado where id = i_id;
    set bono = case
				when v_departamento = 'Ventas' then v_salario*1.10
				when v_departamento = 'TI' then v_salario*1.15
				else v_salario*1.05
				end;
	select bono into nuevo_salario;
end
//
delimiter ;
call bono(5,@bono);
select @bono;