n=input()
a=int(n)
s=res=''
if a>0:
    b=n[::-1]
    for z in range(len(b)):
        if b[z]=='0':
            continue
        else:
            s=s+b[z]
    print(s)        
else:
    x=n[::-1]
    for i in range (len(x)):
        if x[i]=='-':
            break
        elif x[i]=='0':
            continue
        else:
            res=res+x[i]
    print(f'-{res}')        