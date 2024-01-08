import numpy as np 
from sklearn.datasets import make_classification


a,b = make_classification(1000,)

print(f"shape of a: {np.shape(a)}")
print(f"shape of b: {np.shape(b)}")
print(a)
print("--------------")
print(b)
idx = np.where(b == 0)[0]
print("-------------")
print(idx[0])

