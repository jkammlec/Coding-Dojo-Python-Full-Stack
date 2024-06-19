SELECT * FROM usuarios;

-- INSERT INTO tabla (columna1, columna2) VALUES ("Valor1","Valor2");
INSERT INTO usuarios (nombre, edad, direccion_id) VALUES ("Juana",18,2);
DELETE FROM usuarios WHERE id=8;
-- Actualizar un registro
UPDATE usuarios SET edad = 19 WHERE id = 9;