r=int(input())
mat1=[];mat2=[]
for i in range(r):
    il=list(map(int,input().split()))
    mat1.append(il)
for i in range(r):
    Il=list(map(int,input().split()))
    mat2.append(Il)
ans = []
for i in range(r):
    cur = []
    for j in range(r):
        cur.append(abs(mat1[i][j] - mat2[i][j]))
    ans.append(cur)
for i in ans:
    print(*i)