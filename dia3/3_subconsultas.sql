--subconsultas

USE db_g6;

SELECT AVG(salario) FROM empleado;

--quiero saber los empleados que ganan mas del promedio 

SELECT nombre, salario FROM empleado
WHERE salario > (SELECT AVG(salario) FROM empleado);

--subsconsultas en campo

select pais,count(*) as total,avg(salario) as salario_promedio
from empleado
group by pais;

select nombre,salario,(select avg(salario) from empleado) as salario_promedio,
salario - (select avg(salario) from empleado) as diferencia_salario_promedio
from empleado
where salario > (select avg(salario) from empleado);