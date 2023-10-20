n=int(input());a=x=n
s=c=0
while n>0:
    r=n%10
    c+=1
    n=n//10
for i in range (c,0,-1):
    if i>0:
        r=x%10
        s=s+(r**i)
        x=x//10
if s==a:
    print(True)
else:
    print(False)
    