a=input()
l=list(a)
largest=l[0]
for i in range(len(l)):
    if l[i]>largest:
        largest=l[i]
print(largest)        