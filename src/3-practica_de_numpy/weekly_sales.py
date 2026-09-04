import numpy as np

"""Colums = Days"""
"""Rows  = Store branch"""

sales = np.array(
    [
        [1200, 1350, 980, 1420, 1100],
        [850, 920, 1050, 890, 960],
        [1600, 1750, 1580, 1690, 1720],
    ]
)

total_sales_by_branch = sales.sum(axis=1)
comisions = total_sales_by_branch * 0.05
total_sales_by_day = sales.sum(axis=0)

print("Totales por sucursal:", total_sales_by_branch)
print("Comisiones (5%):", comisions)
print("Totales por día:", total_sales_by_day)