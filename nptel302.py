w=input()
w1=w.split()
row=int(w1[0])
col=int(w1[1])
m=[0]*row
for i in range(row) :
	m[i]=[0]*col
k=1
for i in range(row) :
	for j in range(col) :
		m[i][j]=k
		k+=1
for i in range(row) :
	for j in range(col) :
		if j==(col-1) :
			print(m[i][j],end='')
		else :
	  		print(m[i][j],end=' ')
	if i!=(row-1) :
		print("")

