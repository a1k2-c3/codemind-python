n=int(input());c=x=0
a=n;b=n
l=[]
while n>0:
    r=n%10
    if r not in l:
        l.append(r)
    n=n//10
while a>0:
    r=a%10
    if r in l:
        c+=1
    a=a//10
if len(l)==c:
    print('Unique Number')
else:
    print('Not Unique Number')
    