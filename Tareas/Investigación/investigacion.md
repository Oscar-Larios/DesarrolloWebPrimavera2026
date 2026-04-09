# Investigación

## ¿Qué es una transacción?
Una transacción es un conjunto de operaciones SQL que se ejecutan como una sola unidad. Si todo sale bien se confirma con COMMIT. Si algo falla, se revierte con ROLLBACK. Se usa para garantizar que procesos críticos (como transferencias bancarias) no queden a medias. O todo pasa, o nada pasa.

## ¿Cómo evitar que CREATE TABLE falle si la tabla ya existe?
Se usa IF NOT EXISTS en el comando de creación: CREATE TABLE IF NOT EXISTS usuarios (id INT PRIMARY KEY, nombre VARCHAR(100)); Si la tabla ya existe, el comando simplemente no hace nada en lugar de lanzar un error.

## ¿Qué es un trigger o disparador?
Un trigger es código que se ejecuta automáticamente al ocurrir un evento en una tabla (INSERT, UPDATE, DELETE). Por ejemplo, guardar automáticamente en una tabla de auditoría cada vez que se modifica un precio, o verificar antes de una venta que haya stock suficiente y cancelar la operación si no lo hay.

## ¿Qué es SQL Injection?
Es un ataque donde se inserta código SQL malicioso en un campo de entrada que la app pasa directo a la base de datos sin validarlo. Las consecuencias van desde filtración y robo de datos hasta borrado total de la base o control del servidor.

### Casos reales:

1. GhostShell University Attack (2012)
El colectivo de hackers Team GhostShell llevó a cabo un ataque de SQL Injection contra 53 universidades alrededor del mundo, robando y publicando 36,000 registros personales de estudiantes, profesores y personal administrativo. El ataque dejó en evidencia las graves vulnerabilidades de seguridad que existían en las instituciones académicas a nivel global.
https://www.radware.com/cyberpedia/application-security/sql-injection/
 
2. HBGary Hack (2011)
Hackers vinculados al grupo Anonymous explotaron una vulnerabilidad de SQL Injection para infiltrarse en HBGary, una firma de seguridad informática, derribaron su sitio web y filtraron comunicaciones internas confidenciales. El ataque fue una represalia directa luego de que el CEO de la empresa afirmara públicamente haber identificado a miembros clave de Anonymous.
https://www.radware.com/cyberpedia/application-security/sql-injection/
 
3. 7-Eleven Breach (2007)
Un grupo de atacantes usó SQL Injection para comprometer los sistemas de pago de varias empresas, incluyendo la cadena de tiendas 7-Eleven, logrando robar más de 130 millones de números de tarjetas de crédito. Fue una de las mayores brechas de datos de su época y demostró las enormes consecuencias financieras y legales que puede tener una sola vulnerabilidad sin parchar.
https://www.radware.com/cyberpedia/application-security/sql-injection/

## ¿Qué es un ORM y cómo se diferencia del SQL puro?
Un ORM (Object-Relational Mapper) permite interactuar con la base de datos usando el lenguaje de alguna app (Python, JS, etc.) en lugar de escribir SQL directamente. Por ejemplo, Usuario.find(1) en vez de SELECT * FROM usuarios WHERE id = 1. Es más rápido de escribir, más seguro frente a SQL Injection y más fácil de mantener. Sin embargo, el SQL puro sigue ganando cuando necesitas consultas complejas o de alto rendimiento, ya que los ORM a veces generan queries ineficientes.