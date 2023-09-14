a=int(input())
t1=0;t2=1;c=0
l=[0,1]
for i in range(1000):
    t3=t1+t2
    l.append(t3)
    t1=t2
    t2=t3
for z in range(len(l)):
    if l[z]==a:
        c+=1
if c==1:
    print('True')
else:
    print('False')