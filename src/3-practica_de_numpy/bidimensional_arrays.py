import numpy as np

study_hours = np.array(
    [
        [5, 8, 6, 7],
        [10, 9, 11, 8],
        [3, 4, 2, 5],
    ]
)

print(study_hours.shape)
print("Promedio por estudiante:", np.mean(study_hours, axis=1))
print("Promedio por semana:", np.mean(study_hours, axis=0))