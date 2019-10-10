x=[i.lower() for i in input()]
#print(x)
x1='a b c d e f g h i j k l m n o p q r s t u v w x y z 0'.split()
for i in x :
	if i in x1 :
		x1.remove(i)
if x1[0]=='0' :
	print('YES',end="")
else :
	print('NO',end="")