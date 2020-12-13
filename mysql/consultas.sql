-- 1. Seleccionar todas las categorías de productos
SELECT
	DISTINCT cat.id,
	cat.descripcion
FROM
	bd_neptuno.categorias cat
	INNER JOIN bd_neptuno.productos pro ON (cat.id = pro.categoria_id);

-- 2.
-- 3. seleccionar los productos de una categoría.
-- elijo una categoria al azar
SELECT
	prod.id,
	prod.producto
FROM
	bd_neptuno.productos prod
WHERE
	prod.categoria_id = 1;

-- 4. Seleccionar una lista con los datos y Valor de cada producto
SELECT
	prod.id,
	prod.producto,
	prod.precio_unidad
FROM
	bd_neptuno.productos prod;

-- 5. Buscar datos y Valor del producto mas caro y más barato
SELECT -- O(x) = 3 * n
	prod.id,
	prod.producto,
	prod.precio_unidad
FROM
	bd_neptuno.productos prod
WHERE
	prod.precio_unidad = (SELECT MAX(prod.precio_unidad) FROM bd_neptuno.productos prod)
OR
	prod.precio_unidad = (SELECT MIN(prod.precio_unidad) FROM bd_neptuno.productos prod);
