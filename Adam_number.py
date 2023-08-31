n=int(input())
x=n
s=n*n
rev=d=0
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
y=rev*rev
while y>0:
    t=y%10
    d=(d*10)+t
    y=y//10
if d==s:
    print('True')
else:
    print('False')
    