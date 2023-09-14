def auto(n):
    x=n*n;c=s=b=a=0
    while n>0:
        r=n%10
        s=s+r
        c+=1
        n=n//10
    while x>0:
        rem=x%10
        a=a+rem
        b+=1
        if b==c:
            break
        x=x//10
        
    if s==a:
        print('Automorphic Number')
    else:
        print('Not an Automorphic Number')
n=int(input())
auto(n)