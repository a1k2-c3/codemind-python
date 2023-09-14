n=input()
# r=n%10
# if r!=9:
#     n=n+3
# re=n%100
# if re>=60 and re<70:
#     n=n+30
# rem=n%1000
# if rem>=600 and rem<700:
#     n=n+300
# x=n%10000
# if x>=6000 and x<7000:
#     n=n+3000
# print(n)   

l=list(n)
# print(l)
for i in range(len(l)):
    if(int(l[i])==6):
        l[i]='9'
        break
res=""
for i in l:
    res+=i
print(res)