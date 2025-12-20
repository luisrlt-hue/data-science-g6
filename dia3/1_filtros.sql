--Filtros

SELECT *from empleado WHERE pais='Peru';

SELECT *from empleado WHERE salario>5000

SELECT  *from empleado WHERE pais='Peru' AND salario>5000;

SELECT  *from empleado
WHERE salario>5000
AND (pais='Peru' OR pais='Colombia');

SELECT * FROM empleado
WHERE pais IN ('Argentina','Chile');

SELECT * FROM empleado
WHERE salario BETWEEN 10000 AND 15000;


