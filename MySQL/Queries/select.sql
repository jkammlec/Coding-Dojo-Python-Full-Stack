-- Queries = Consultas
-- SELECTS -> buscar/seleccionar registros de una tabla
SELECT * FROM usuarios;
SELECT nombre,edad FROM usuarios;
SELECT nombre,edad FROM usuarios WHERE id = 2;
SELECT nombre,edad FROM usuarios WHERE nombre LIKE "Alejandro";
SELECT * FROM usuarios WHERE nombre LIKE "Al%"; -- empieza con Al
SELECT * FROM usuarios WHERE nombre LIKE "%o"; -- termina en letra o
SELECT * FROM usuarios WHERE nombre LIKE "%o" AND edad > 24;
SELECT * FROM usuarios WHERE nombre LIKE "%o" OR edad > 24;
SELECT * FROM usuarios WHERE nombre LIKE "%a%";
SELECT * FROM usuarios WHERE nombre LIKE "%a%" ORDER BY edad ASC; -- por defecto es ascendente

-- SELECT columnas FROM tabla WHERE condicional ORDER BY columna LIMIT 0,cantidad

SELECT * FROM usuarios WHERE nombre LIKE "%a%" ORDER BY edad ASC LIMIT 0,3; -- LIMIT COMIENZO,FIN

-- 1:1 Desplegar la unión entre usuarios y direcciones
-- Unir en base a direccion_id (columna de usuarios, llave foránea) = id de la tabla de direcciones
SELECT * FROM usuarios JOIN direcciones ON direccion_id = direcciones.id ORDER BY ciudad ASC;

-- 1:n Desplegar la unión entre pedidos y usuarios
-- Unir en base a usuario_id (tabla de pedidos, llave foránea) = id de la tabla usuarios
SELECT * FROM pedidos JOIN usuarios ON usuario_id = usuarios.id; -- solo los que coinciden en ambas tablas

-- 1:n
SELECT * FROM usuarios LEFT JOIN pedidos ON usuarios.id = usuario_id; -- TODOS los de la primera tabla, y los coincidentes de la segunda

-- n:n
SELECT *  FROM usuarios JOIN usuarios_has_hobbies ON usuarios.id = usuarios_has_hobbies.usuario_id JOIN hobbies ON
hobbies.id = usuarios_has_hobbies.hobbie_id;

SELECT nombre,actividad FROM usuarios JOIN usuarios_has_hobbies ON usuarios.id = usuarios_has_hobbies.usuario_id JOIN hobbies ON
hobbies.id = usuarios_has_hobbies.hobbie_id;

SELECT UPPER(nombre) as nombre_mayus FROM usuarios;
SELECT LOWER(nombre) as nombre_min FROM usuarios;

SELECT SUM(total) FROM pedidos; -- Suma de la colummna total
SELECT AVG(total) FROM pedidos; -- Promedio de la columna total
SELECT COUNT(*) FROM pedidos; -- Contando el total de registros (filas)
SELECT SUM(total),usuario_id FROM pedidos GROUP BY usuario_id;
SELECT AVG(total),usuario_id,nombre FROM pedidos JOIN usuarios ON usuario_id = usuarios.id GROUP BY usuario_id;
SELECT COUNT(*),usuario_id,nombre FROM pedidos JOIN usuarios ON usuario_id = usuarios.id GROUP BY usuario_id;