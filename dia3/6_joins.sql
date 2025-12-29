use db_g6

--JOINS

--A ALUMNO
--bB NOTAS


INSERT INTO alumno (nro_documento,nombre) VALUES('1001','Gabriel Sanchez');
--LEFT JOIN
SELECT alumno.nombre,AVG (nota.nota) as nota_promedio
FROM alumno LEFT JOIN nota ON nota.alumno_id=alumno.id
GROUP BY alumno.nombre;


SELECT alumno.nombre,AVG (nota.nota) as nota_promedio
FROM alumno LEFT JOIN nota ON nota.alumno_id=alumno.id
GROUP BY alumno.nombre;

--right JOIN
INSERT INTO curso (nombre) VALUES ('Nump y Pandas');

SELECT curso.nombre,AVG (nota.nota) as nota_promedio
FROM nota RIGHT JOIN curso ON nota.curso_id=curso.id
GROUP BY curso.nombre;

---INNER JOIN
SELECT alumno.nombre,curso.nombre,nota.nota
FROM nota
INNER JOIN alumno ON nota.alumno_id=alumno.id
INNER JOIN curso ON nota.curso_id=curso.id
ORDER BY alumno.nombre;

