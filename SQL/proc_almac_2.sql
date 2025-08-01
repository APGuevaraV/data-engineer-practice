/*
desactivar clientes sin compras en más de 1 año
*/

delimiter //
create procedure DeshabilitarClientesInactivos()
begin
	with CTE_menor_fecha_actual as(
	select clientes.cliente_id 
    from clientes 
    inner join ventas_fecha 
    on clientes.cliente_id = ventas_fecha.cliente_id
    where ventas_fecha.fecha < DATE_SUB(NOW(),INTERVAL 1 YEAR)
	)
	update clientes set activo = 0 where cliente_id in (select cliente_id from CTE_menor_fecha_actual);
    select 'Actualizado correctamente' as status;
end
 //
delimiter ;

call DeshabilitarClientesInactivos;