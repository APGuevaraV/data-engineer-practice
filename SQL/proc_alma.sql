delimiter //
create procedure AgregarProducto (
	nombre varchar(100),
	precio decimal(10,2),
    stock int
    )
begin
		IF precio <= 0 THEN
			SELECT 'El precio debe ser mayor a 0' AS status;
		ELSEIF stock < 0 THEN
			SELECT 'La cantidad de stock no puede ser negativa' AS status;
		ELSE
			INSERT INTO Productos(nombre, precio, stock)
			VALUES (nombre, precio, stock);
			SELECT 'Agregado correctamente' AS status;
    END IF;
end //
delimiter ;

delimiter //
create procedure ActualizarStock (
	product_id int,
    increment_stock int
    )
begin
		declare count_product int;
		declare stock_qty int ;
        declare new_stock int ;
        select count(*) into count_product from productos 
        where producto_id = product_id ;
		
		if count_product > 0 THEN
			select stock into stock_qty from productos where producto_id = product_id;
            set new_stock = stock_qty + increment_stock;
            if new_stock < 0 THEN
				select 'No se puede reducir el stock por debajo' as status;
			else
				update productos set stock = new_stock where producto_id = product_id ;
				select 'Actualizado correctamente';
			end if;
        else 
			select 'Id de Producto no existe';
        end if;
end //
delimiter ;

call AgregarProducto('dento',4,10);
call ActualizarStock(2,2);

delimiter //
create procedure VentasPorCliente(clienteId int,fechaInicio date, fechafin date)
begin
	select * from ventas 
    where  fecha between fechaInicio and fechafin
    AND cliente_id = clienteId
    ORDER BY fecha DESC;
end //
delimiter ;

call VentasPorCliente('8','2024-07-01','2024-07-30');