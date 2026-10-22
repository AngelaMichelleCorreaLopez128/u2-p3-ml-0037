import numpy as np
# Angela Correa NC = 0037 Fecha 22 octubre de 2026
n0037=np.array([10, 20, 30, 40, 50])
print(n0037)
print(n0037[0])
print(n0037[-1])
print(n0037[-2])
print("----------------------------------")
n0037=np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(n0037)
print(n0037[0, 0])
print(n0037[1, 2])
print(n0037[-1, -1])
print(n0037[-2, -2])
print("----------------------------------")

n0037=np.array([
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])
print(n0037)
print(n0037[0,0,0])
print(n0037[1,1,2])
print(n0037[-1,-1,-2])
print("Angela Correa NC = 0037")