n=int(input());a=n
s=n**2;rev=c=0
while n>0:
    r=n%10
    rev=(rev*10)+r
    n=n//10
x=rev**2    
while x>0:
     rem=x%10
     c=(c*10)+rem
     x=x//10
if c==s:
    print(True)
else:
    print(False)