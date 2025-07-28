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

