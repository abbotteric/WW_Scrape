import sys
import numpy as np

x = np.array([[1,2,3],[4,5,6]],np.int32)
print type(x)

print x[1,:]

x[2,:] = [7,8,9]

print x[2,:]