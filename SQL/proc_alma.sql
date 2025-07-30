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


delimiter //
create procedure TotalVentasPorProducto (productoId int)
	begin
	select producto_id,
	sum(cantidad * precio_unitario)
	from DetalleVenta 
	where producto_id = productoId
	group by producto_id ;
end //

call TotalVentasPorProducto(3);


delimiter //
create procedure ClienteTopCompras ()
	begin
		select  
        c.cliente_id,
		c.nombre AS cliente_nombre,
		sum(v.total) as total_compra
		from Ventas v
        INNER JOIN Clientes c ON v.cliente_id = c.cliente_id
		group by c.cliente_id,c.nombre
        order by total_compra desc 
        limit 1;
	end //
delimiter ;
call ClienteTopCompras;


delimiter //
create procedure UpsertCliente( in clienteId int,in nombreIn varchar(100), in correoIn varchar(100))
	begin
		
        if exists (select 1 from clientes where cliente_id = clienteId) THEN
			Update clientes 
            set nombre = nombreIn ,
				correo = correoIn
			where cliente_id= clienteId;
            select 'Actualizado correctamente' as status;
		ELSE
			insert into clientes(cliente_id,nombre,correo) values(clienteId,nombreIn,correoIn);
            select 'Nuevo registro' as status;
		end if;
    end //
delimiter ;


delimiter //
create procedure AumentarPreciosCategoria(in categoriaId int , in porcentaje float)
begin
	if exists (select 1 from categorias where categoria_id = categoriaId) and porcentaje > 0 THEN
		update productos 
		set precio = precio*(1+porcentaje/100)  
		where producto_id in (
				select p.producto_id 
				from (select producto_id from productos 
				where categoria_id = categoriaId) as p
                );
        select 'actualizada la categoría' as status;
	else
    select 'Categoría no encontrada' as status;
    end if;
end
 //
delimiter ;


delimiter //
create procedure TotalVentasProducto(in productoId int, out total_ventas float)
begin
	
    SELECT IFNULL(SUM(cantidad * precio_unitario), 0)
	into total_ventas
    from DetalleVenta where producto_id = productoId;
end //
delimiter ;

CALL TotalVentasProducto(1, @total);
SELECT @total as totalvendido;