import sys
import numpy as np
import re

f = open('PPlus.csv','r+')
f.readline()
line = f.readline()
sum = 0
count = 0
while (line):
	count = count + 1
	m = re.search('(.*),(.*),(.*),(.*),([0-9]*)',line)
	sum = sum+int(m.group(5))
	line = f.readline()
	
mean = float(sum)/float(count)
f.seek(0)

SS_err = 0
SS_tot = 0
array = np.array([1,1,1,1,1,1,1,1],np.int32)
answers = np.array([1],np.int32)

f.readline()
line = f.readline()
while (line):
	m = re.search('(.*),(.*),(.*),(.*),([0-9]*)',line)
	w = int(m.group(1))
	x = int(m.group(2))
	y = int(m.group(3))
	z = int(m.group(4))
	a = int(m.group(5))
	pp = 0.255018619583*w + 0.119532905297*x + 0.0859900481541*y + -0.079267094703*z#+5.01605136438e-05*w*w + -0.000521268057785*x*x + 0.000193017656501*y*y + -2.12680577849e-05*z*z	
	SS_tot = SS_tot + (a - mean)*(a - mean)
	SS_err = SS_err + (a - pp)*(a-pp)
	line = f.readline()
	
print 'R^2 = '+str(1.0-(float(SS_err)/float(SS_tot)))