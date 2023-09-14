n=int(input())
l=[]
c=0
for i in range(0,1000):
    a=i*(i+1)
    l.append(a)
for i in l:
    if i==n:
        c+=1
if c==1:
    print('YES')
else:
    print('NO')