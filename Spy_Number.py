n=int(input())
s=n
e=0
p=1
while n>0:
    rem=n%10
    e=e+rem
    n=n//10
while s>0:
    r=s%10
    p=p*r
    s=s//10
if p==e:
    print('Spy Number')
else:
    print('Not Spy Number')