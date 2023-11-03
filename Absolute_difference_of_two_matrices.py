r=int(input())
mat1=[];mat2=[]
for i in range(r):
    il=list(map(int,input().split()))
    mat1.append(il)
for i in range(r):
    Il=list(map(int,input().split()))
    mat2.append(Il)
for i in range(r):
    for j in range(r):
        if (j+1)==r:
            print(abs(mat1[i][j]-mat2[i][j]))
        else:
            print(abs(mat1[i][j]-mat2[i][j]),end=" ")