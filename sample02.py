m=int(input('rows'))
n=int(input('coloumns'))
a=[0]*m
for i in range(m) :
	a[i]=[0]*n

x=1
for i in range(m) :
	for j in range(n) :
		
		a[i][j]=x
		x*=2

for i in range(m) :
	for j in range(n):
		print(a[i][j],end='  ')
	print('')
	#print('')


