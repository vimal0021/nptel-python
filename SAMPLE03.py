from random import randint
a1=int(input())
a=[]
b=[]
for i in range(0,a1) :
	a.append(int(input()))
	
b=a
b.sort()
while True :
	if a==b :
		print(*a,end='')
		break
	else :
		n1=randint(0,a1+1)
		n2=randint(0,a1+1)
		m1=a[n1]
		m2=a[n2]
		a[n1]=m2
		a[n2]=m1

