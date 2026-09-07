# Preguntas de Razonamiento

## ¿Por qué diagnosticar el dataset completo (forma, nulos) antes de limpiar nada, en vez de empezar a limpiar directamente desde la primera columna que veas?

Porque el diagnóstico inicial te permite entender la calidad y estructura de los datos antes de modificarlos. Si empiezas a limpiar directamente, podrías tomar decisiones incorrectas o perder información importante.

---

## ¿Qué pasaría si rellenaras Budget con 0 en vez de eliminar esas filas? ¿Cómo afectaría eso a la columna Ganancia que vas a crear en la próxima etapa?

Si rellenara la columna Budget con 0, por ejemplo, estaría asumiendo que algunas películas no tuvieron ningún costo de producción, lo cual no es realista. Hacer esto crearía datos que no son reales, lo que podría afectar el análisis de estos.

---

## Ganancia se calcula restando (WorldGross - Budget). ¿Qué representaría, en cambio, una columna que dividiera WorldGross entre Budget? ¿En qué caso preferirías esa versión en vez de la resta?

Eso representaría el retorno de la inversión. Por ejemplo, si el presupuesto fue de 1 millón y se ganaron 3, tendríamos un ROI del 200%.

---

## ¿Qué habría pasado si hubieras intentado ordenar por Ganancia antes de limpiar los nulos de WorldGross y Budget en la Etapa 2? ¿Por qué el orden en que se hacen las etapas importa aquí?

Algunas películas no tendrían una ganancia asignada, ya que la operación habría arrojado un (NaN), porque no es posible calcular una resta cuando falta uno de los operadores.

---

## De los géneros con más películas en el dataset (Comedia, Acción, Drama), ¿cuál tiene el promedio de calificación de crítica más alto? ¿Te sorprende, o era lo que esperabas?

Drama, no tenía ninguna expectativa con el resultado, por lo que tampoco me generó sorpresa.

---

## ¿Por qué guardar el resultado en un archivo nuevo (hollywood_limpio.csv), en vez de sobrescribir el archivo original hollywood.csv que descargaste?

Es mejor guardar el resultado en un archivo nuevo para conservar una copia del archivo original sin modificaciones.

---

# Escenarios: ¿qué harías si...?

## ESCENARIO 1

### Si el dataset tuviera una columna de fechas completas (día, mes y año) en vez de solo el año, ¿qué tendrías que verificar antes de poder ordenar el dataset cronológicamente por esa columna?

Verificar la consistencia y el formato para poder trabajarlos uniformemente. Si algunas fechas estuvieran como texto o en formatos diferentes, primero las convertiría para garantizar que las operaciones arrojen el resultado esperado.

---

## ESCENARIO 2

### Si quisieras aplicar este mismo pipeline a un dataset completamente distinto (por ejemplo, canciones con su artista, género y número de reproducciones), ¿qué partes de tu código cambiarían, y cuáles seguirían exactamente igual?

Se mantendrían igual las operaciones de carga y guardado. Lo que cambiaría serían las operaciones realizadas con columnas específicas, ya que cambiaría el proceso porque el contexto no es el mismo. Por ejemplo, la columna exitosa se debe considerar si se define por ventas o por reproducciones.

---

## ESCENARIO 3

### Si una columna nueva tuviera 95% de sus valores nulos (mucho peor que Genre, que tenía cerca del 29%), ¿seguirías rellenándola de la misma forma? ¿Qué harías distinto, y por qué?

Evaluaría si realmente aporta valor al análisis. En este caso la eliminaría porque hay muy poca información relevante.