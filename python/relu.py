import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0,x)

print (relu(12))
print (relu(-12))
print (relu(-1))
print (relu(2353))
