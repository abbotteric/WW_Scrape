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
	array = np.vstack((array,[w,x,y,z,w*w,x*x,y*y,z*z]))	
	answers = np.vstack((answers,[a]))
	line = f.readline()

A = array[1:,:]
Y = answers[1:,:]

temp = np.dot(A.transpose(),A)
inv = np.linalg.inv(temp)

temp = np.dot(A.transpose(),Y)
ans = np.dot(inv,temp)

if(len(sys.argv) > 1):
	print 'pp = '+str(ans[0,0])+'*fat + '+str(ans[1,0])+'*carbs + '+str(ans[2,0])+'*protein + '+str(ans[3,0])+'*fiber +'+str(ans[4,0])+'*fat^2 + '+str(ans[5,0])+'*carbs^2 + '+str(ans[6,0])+'*protein^2 + '+str(ans[7,0])+'*fiber^2'
else:
	print 'pp = '+str(ans[0,0])+'*fat + '+str(ans[1,0])+'*carbs + '+str(ans[2,0])+'*protein + '+str(ans[3,0])+'*fiber'
