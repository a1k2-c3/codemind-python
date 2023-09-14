def spy(n):
    x=n
    s=0
    p=1
    while n>0:
        r=n%10
        s=s+r
        n=n//10
    while x>0:
        rem=x%10
        p=p*rem
        x=x//10
    if s==p:
        print('Spy Number')
    else:
        print('Not Spy Number')
n=int(input())
spy(n)