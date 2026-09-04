import numpy as np

data_usage = np.array([2.3, 5.1, 1.8, 8.4, 3.6, 4.2, 6.9])

print("Promedio:", round(np.mean(data_usage), 2))
print("Máximo:", np.max(data_usage))
print("Mínimo:", np.min(data_usage))
print("Desviación estándar:", round(np.std(data_usage), 2))