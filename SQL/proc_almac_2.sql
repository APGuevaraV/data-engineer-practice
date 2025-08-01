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

call DeshabilitarClientesInactivos();


delimiter //
create procedure ResumenVentasDiario(IN fecha_inicio DATE, IN fecha_fin DATE)
begin
	with CTE_Ventas_por_dia as(
		select fecha,
        count(*) as total_ventas,
        sum(total) as total_ingresos
        from ventas_fecha group by fecha
    )
    select * from CTE_Ventas_por_dia where fecha 
    between fecha_inicio AND fecha_fin;
end
//
delimiter ;

call ResumenVentasDiario('2025-06-01', '2025-07-31');