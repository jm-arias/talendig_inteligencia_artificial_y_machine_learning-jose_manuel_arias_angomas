# Preguntas de Razonamiento

## ¿Por qué diagnosticar el dataset completo (forma, nulos) antes de limpiar nada, en vez de empezar a limpiar directamente desde la primera columna que veas?

Porque el diagnóstico inicial permite entender la calidad y la estructura de los datos antes de modificarlos. Si se empieza a limpiar directamente, se podrían tomar decisiones incorrectas o perder información importante sin saber realmente cuál era el estado original del dataset.

---

## ¿Qué pasaría si rellenaras `Budget` con 0 en vez de eliminar esas filas? ¿Cómo afectaría eso a la columna `Ganancia` que vas a crear en la próxima etapa?

Si rellenara la columna `Budget` con 0, estaría asumiendo que algunas películas no tuvieron ningún costo de producción, lo cual no es realista. Hacer esto crearía datos que no son reales y podría afectar negativamente el análisis posterior.

---

## Ganancia se calcula restando (`WorldGross - Budget`). ¿Qué representaría, en cambio, una columna que dividiera `WorldGross` entre `Budget`? ¿En qué caso preferirías esa versión en vez de la resta?

Esa operación representaría el retorno de la inversión (ROI). Por ejemplo, si el presupuesto fue de 1 millón y la película recaudó 