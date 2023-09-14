n=int(input())
l=[];c=0
for i in range(0,1000):
    a=i*i
    l.append(a)
for i in range(len(l)):
    if l[i]==n:
        c+=1
if c==1:
    print('True')
else:
    print('False')