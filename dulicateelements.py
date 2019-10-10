x=input().split()
x1=[]
x2=[]
for i in x :
	x1.append(int(i))
for i in x1 :
	if i in x2:
		continue
	else :
		x2.append(i)
	print(i,end=" ")

