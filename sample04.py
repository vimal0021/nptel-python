x=input()
x=x.split()
n=int(x[0])
v1=int(x[1])
v2=int(x[2])
if (((2**0.5)*n)/v1) < ((2*n)/v2) :
	print("Walk",end="")
else :
	print("Cab",end="")