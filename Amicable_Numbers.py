def amicable(a,b):
    s=x=0
    for i in range(1,a):
        if a%i==0:
            s=s+i
    for z in range(1,b):
        if b%z==0:
            x=x+z
    if s==b and x==a:
        print('Amicable')
    else:
        print('Not Amicable')
a=int(input());b=int(input())
amicable(a,b)