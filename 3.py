v=['0','1','2','5','6','8','9']
g=int(input())
l=[]
a=1
t=1
while(t<=g):
    str1=str(a)
    c=0
    for i in str1:
        if(i in v):
            c+=1
    if(c==len(str1)):
        l.append(str1)
        t+=1
    a+=1
z=l[len(l)-1]
z=int(z)
print(z)
