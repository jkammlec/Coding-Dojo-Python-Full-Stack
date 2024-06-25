-- ¿Qué consulta ejecutarías para obtener todos los países que hablan español? Tu consulta debe devolver el nombre del país, el idioma y el porcentaje de habla del idioma.  Tu consulta debe ordenar el resultado por porcentaje de habla del idioma en orden descendente. (1)
SELECT nombre,idioma,porcentage FROM paises JOIN idiomas ON pais_id = paises.id WHERE idioma = 'Español' ORDER BY porcentage DESC;
-- ¿Qué consulta ejecutarías para mostrar el número total de ciudades de cada país?  Tu consulta debe devolver el nombre del país, el idioma y el número total de ciudades. Tu consulta debe ordenar el resultado por el número de ciudades en orden descendente. (3)
SELECT paises.nombre, idiomas.idioma, COUNT(ciudades.id) AS numero_ciudades FROM paises JOIN ciudades 
ON paises.id = pais_id JOIN idiomas ON paises.id = idiomas.pais_id GROUP BY paises.nombre, idiomas.idioma
ORDER BY numero_ciudades DESC;
-- ¿Qué consulta ejecutarías para obtener todos ciudades de Chile con una población mayor a 200,000? Tu consulta debe ordenar el resultado por población en orden descendente. (1)
SELECT paises.nombre, ciudades.nombre, ciudades.poblacion FROM paises JOIN ciudades ON pais_id = paises.id WHERE paises.nombre = 'Chile' AND ciudades.poblacion > 200000 ORDER BY ciudades.poblacion DESC;
-- ¿Qué consulta ejecutarías para obtener todos los idiomas en cada país con un porcentaje de habla mayor a 89%? Tu consulta debe ordenar el resultado por porcentaje de habla en orden descendente. 
SELECT paises.nombre, idioma, porcentage FROM paises JOIN idiomas ON pais_id = paises.id WHERE porcentage > 89 ORDER BY porcentage DESC;
-- ¿Qué consulta ejecutarías para obtener todos los países con un área de superficie menor a 501 y población mayor a 100,000?
SELECT nombre, area_superficie, poblacion FROM paises WHERE area_superficie < 501 AND poblacion > 100000 ORDER BY area_superficie;
-- ¿Qué consulta ejecutarías para obtener países en el que el tipo de gobierno es República, un capital superior a 2000 y una esperanza de vida mayor a 78 años?  (1)
SELECT nombre, tipo_gobierno, capital, esperanza_vida FROM paises WHERE tipo_gobierno = 'República' AND capital > 2000 AND esperanza_vida > 78 ORDER BY nombre;
-- ¿Qué consulta ejecutarías para obtener todas las ciudades de Colombia dentro del distrito de Valle con una población mayor a 200,000 habitantes?  La consulta debe devolver el nombre del país, el nombre de la ciudad, el distrito y la población.  (2)
SELECT paises.nombre, ciudades.nombre, distrito, ciudades.poblacion FROM ciudades JOIN paises ON pais_id = paises.id WHERE paises.nombre = 'Colombia' AND distrito = 'Valle' AND ciudades.poblacion > 200000;
-- ¿Qué consulta ejecutarías para resumir el número de países en cada región? Tu consulta debe mostrar el nombre de la región y el número de países. Además, debe ordenar el resultado por el número de países en orden descendente. (2)
SELECT region, COUNT(*) AS numero_paises FROM paises GROUP BY region ORDER BY numero_paises DESC;