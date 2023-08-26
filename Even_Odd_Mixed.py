n=int(input())
y=n
c=s=x=0
while n>0:
    w=n%10
    if True:
        x+=1
    n=n//10    
while y>0:
    rem=y%10
    if rem%2==0:
        c+=1
    elif rem%2==1:
        s+=1
    y=y//10

if c==x:
    print('Even')
elif s==x:
    print('Odd')
else:
    print('Mixed')