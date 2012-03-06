import sys
import numpy as np
import re

f = open('PPlus.csv','r+')
f.readline()
line = f.readline()
while (line):
	m = re.search('(.*),(.*),(.*),(.*),([0-9]*)',line)
	print m.group(3)
	line = f.readline()

x = np.array([[1,2,3],[4,5,6]],np.int32)
print type(x)

print x[1,:]

x = np.vstack((x,[7,8,9]))

print x[2,:]