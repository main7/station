# -*- unicode:utf-8 -*-
import math
def func(a,b,c):
	k=b*b-4*a*c
	n=-b/2;
	if a == 0 :
		if b!=0:
			print('x=%f'% (-c/b))
		else:
			print('无解')
	else:
		if k>0:
			print('x=%f' % (n+math.sqrt(k)/2/a))
			print('x=%f'% (n-math.sqrt(k)/2/a))
		elif k==0:
			print('x=%f'% (n+math.sqrt(k)/2/a))
		else :
			print('虚根')
a=input('输入a:')
b=input('输入b:')
c=input('输入c:')
a=float(a)
b=float(b)
c=float(c)
func(a,b,c)