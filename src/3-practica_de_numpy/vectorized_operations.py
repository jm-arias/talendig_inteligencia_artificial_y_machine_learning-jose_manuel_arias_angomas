import numpy as np

comisiones = np.array([120.50, 340.00, 89.75, 210.25])
comisiones_con_bono = comisiones * 1.10
print(comisiones_con_bono.round(2))