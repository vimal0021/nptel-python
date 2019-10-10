
m=int(input('order '))
a=[0]*m
for i in range(m) :
    a[i]=[0]*m

x=1
for i in range(m) :
    for j in range(m) :
        a[i][j]=x
        x+=1
for i in range(m) :
    for j in range(m):
        print(a[i][j],end='  ')
    print('')

global y
b=[0]*((m**2))

def cspiral(rs=0,re=m,cs=0,ce=m) :
    
    y=0

    for i in range(rs,re) :
        b[y]=a[i][cs]
        y+=1
        print(b)  
    
    for i in range(cs+1,ce-1):
        b[y]=a[re-1][i]
        y+=1
        print(b)  
        
    for i in reversed(range(rs,re)):
        b[y]=a[i][ce-1]
        y+=1
        print(b)  
    
    for i in reversed(range(cs+1,ce-1)):
        b[y]=a[rs][i]
        y+=1
        print(b)  
    print("-----------------",b)   
    if m%2==0 :
        if b[(m**2)-1]==a[(m-1)//2][m//2] :
            pass
        else :
            cspiral(rs+1,re-1,cs+1,ce-1)
    else :
        if b[(m**2)-1]==a[m//2][m//2]:
            pass
        else :
            cspiral(rs+1,re-1,cs+1,ce-1)
        


print("#"*20)
cspiral()
print(b)

