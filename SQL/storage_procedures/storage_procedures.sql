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
