def poli(n):
    rev=0
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    return rev
n=int(input());x=n
a=poli(n)
if a==x:
    print(True)
else:
    print(False)