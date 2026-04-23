-- 1. Todos los chismes registrados
SELECT * 
FROM chismes;

-- 2. Solo los chismes reales
SELECT * 
FROM chismes 
WHERE es_real = 1;

-- 3. Chismes inventados
SELECT * 
FROM chismes 
WHERE es_real = 0;

-- 4. Chismes con monto de silencio mayor a 500
SELECT * 
FROM chismes 
WHERE monto_silencio > 500;

-- 5. Chismes con gravedad mayor o igual a 4
SELECT quien_dijo, sobre_quien, chisme 
FROM chismes 
WHERE nivel_gravedad >= 4;

-- 6. Chismes sobre Ana
SELECT sobre_quien, chisme, quien_dijo 
FROM chismes 
WHERE sobre_quien = 'Ana';

-- 7. Chismes entre dos fechas
SELECT chisme, fecha 
FROM chismes 
WHERE fecha BETWEEN '2024-01-01' AND '2024-09-30';

-- 8. Cuántos chismes se dijeron por año
SELECT strftime('%Y', fecha) AS anio, COUNT(*) AS total_chismes
FROM chismes
GROUP BY strftime('%Y', fecha);

-- 9. Cuántos chismes por año solo en enero
SELECT strftime('%Y', fecha) AS anio, COUNT(*) AS total_chismes_enero
FROM chismes
WHERE strftime('%m', fecha) = '01'
GROUP BY strftime('%Y', fecha);

-- 10. Chismes agrupados por año y mes (antes de marzo)
SELECT strftime('%Y', fecha) AS anio, 
       strftime('%m', fecha) AS mes, 
       COUNT(*) AS total_chismes
FROM chismes
WHERE strftime('%m', fecha) < '03'
GROUP BY strftime('%Y', fecha), strftime('%m', fecha);

-- 11. Años donde se dijeron más de 12 chismes
SELECT strftime('%Y', fecha) AS anio, COUNT(*) AS total_chismes
FROM chismes
GROUP BY strftime('%Y', fecha)
HAVING total_chismes > 12;

-- 12. Meses donde el total pagado por silencio supera 900
SELECT strftime('%m', fecha) AS mes, SUM(monto_silencio) AS total_pagado
FROM chismes
GROUP BY mes
HAVING total_pagado > 900;

-- 13. Promedio del monto de silencio
SELECT AVG(monto_silencio) AS promedio_silencio
FROM chismes;

-- 14. Promedio de gravedad por categoría
SELECT categoria, AVG(nivel_gravedad) AS promedio_gravedad
FROM chismes
GROUP BY categoria;

-- 15. Categorías con más de 2 chismes
SELECT categoria, COUNT(*) AS total
FROM chismes
GROUP BY categoria
HAVING total > 2;

-- 16. Personas que recibieron más de 500 en pagos de silencio
SELECT sobre_quien, SUM(monto_silencio) AS total_recibido
FROM chismes
GROUP BY sobre_quien
HAVING total_recibido > 500;

-- 17. Chismes con testigos distintos de cero
SELECT * 
FROM chismes 
WHERE testigos <> 0;

-- 18. Chismes de gravedad entre 2 y 4
SELECT * 
FROM chismes 
WHERE nivel_gravedad BETWEEN 2 AND 4;

-- 19. Chismes de la categoría trabajo
SELECT * 
FROM chismes 
WHERE categoria = 'trabajo';

-- 20. Chismes contados por lugar
SELECT lugar, COUNT(*) AS total_chismes
FROM chismes
GROUP BY lugar;

-- 21. Lugares donde se dijeron más de 3 chismes
SELECT lugar, COUNT(*) AS total_chismes
FROM chismes
GROUP BY lugar
HAVING total_chismes > 3;

-- 22. Personas que dijeron chismes con promedio de gravedad mayor a 3
SELECT quien_dijo, AVG(nivel_gravedad) AS promedio_gravedad
FROM chismes
GROUP BY quien_dijo
HAVING promedio_gravedad > 3;
