import numpy as np

# 求二元一次线性方程组的解
a = np.array([[3, -2], [2, 1]])
b = np.array([12, 1])
d = np.linalg.solve(a, b)
print(d)
