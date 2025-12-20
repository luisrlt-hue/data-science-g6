use db_g6;

--funciones de agrupacion

SELECT MAX(salario) FROM empleado;

SELECT MIN(salario) FROM empleado;  

SELECT AVG(salario) FROM empleado; 

SELECT MAX(salario),MIN(salario),AVG(salario) FROM empleado;

SELECT DISTINCT pais FROM empleado;

--seleccionar el total de empleados por pais

SELECT pais, COUNT(*) FROM empleado GROUP BY pais
ORDER BY COUNT(*) DESC; 

SELECT pais,area,
COUNT(*),max(salario),min(salario),avg(salario)
FROM empleado
WHERE salario > 5000
GROUP BY pais,area
ORDER BY pais,area;

SELECT pais,COUNT(*)
FROM empleado
GROUP BY pais
HAVING COUNT(*)>100;



