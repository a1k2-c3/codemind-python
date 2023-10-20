def poli(n):
    a=n
    rev=0
    while n>0:
        r=n%10
        rev=(rev*10)+r
        n=n//10
    if rev==a:
        return True
    else:
        return False
n=int(input())
y=0
m=0
x=0
b=0
i=1;z=1
while True:
    y=n-i
    if poli(y):
        x=abs(n-y)
        break
    i+=1
while(True):
    m=n+z
    if poli(m):
        b=abs(n-m)
        break
    z+=1
if x<b:
    print(y)
elif x==b:
    print(y,m,sep=' ')
else:
    print(m)
    
    