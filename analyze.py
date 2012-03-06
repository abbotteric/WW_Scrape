import sys
import numpy as np
import re

f = open('PPlus.csv','r+')
f.readline()
line = f.readline()
array = np.array([1,1,1,1,1,1,1,1],np.int32)
answers = np.array([1],np.int32)
while (line):
	m = re.search('(.*),(.*),(.*),(.*),([0-9]*)',line)
	w = int(m.group(1))
	x = int(m.group(2))
	y = int(m.group(3))
	z = int(m.group(4))
	a = int(m.group(5))
	print m.group(0)
	array = np.vstack((array,[w,x,y,z,w*w,x*x,y*y,z*z]))	
	answers = np.vstack((answers,[a]))
	line = f.readline()

A = array
Y = answers

print A

temp = np.dot(A.transpose(),A)
inv = np.linalg.inv(temp)

temp = np.dot(A.transpose(),Y)
ans = np.dot(inv,temp)

print 'pp = '+str(ans[0,0])+'*fat + '+str(ans[1,0])+'*carbs + '+str(ans[2,0])+'*protein + '+str(ans[3,0])+'*fiber'
