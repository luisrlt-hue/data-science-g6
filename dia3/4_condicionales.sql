
SELECT
nombre,salario,
CASE
    WHEN salario >=5000 THEN 'Alto'
    WHEN salario >= 3000 THEN 'Medio'
    ELSE 'Bajo'
END AS nivel_salarial
FROM empleado;

--clasificar empleados por nacional y extrajenros

SELECT
nombre,pais,
CASE
    WHEN pais = 'Peru' THEN 'Nacional'
    ELSE 'Extranjero'
END AS tipo_empleado
FROM empleado;
