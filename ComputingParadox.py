l=int(input())
A=input()
A1=A.split()
a=[]
b=[]
for i in A1 :
	a.append(int(i))
	b.append(int(i))
b.sort()
k=int(input())
k1=a[k-1]
print(b.index(k1)+1,end="")