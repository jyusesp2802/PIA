"""
Haz lo mismo que en el ejercicio anterior pero usando la libreria numpy

Autor: Jaime Yust
Fecha:26/11/2025

"""

import numpy as np

rows = 3
columns = 2
low_num = 100
big_num = 999
width_num = 5

array = np.random.randint(low_num, big_num + 1, size=(rows, columns))

for row in array:
    for n in row:
        print(f"{n:{width_num}} ", end="")
    print(f"| {row.sum():{width_num}}")

len_sep = ((width_num + 1) * (columns + 1) + 1)
print("-" * len_sep)

sum_columns = array.sum(axis=0)
sum_total = sum_columns.sum()

for sc in sum_columns:
    print(f"{sc:{width_num}} ", end="")
print(f"| {sum_total:{width_num}}")
