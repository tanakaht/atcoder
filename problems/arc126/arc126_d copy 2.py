M=1<<99
N,K=map(int,input().split())
A=list(map(int,input().split()))
p=[bin(x).count("1") for x in range(1<<K)]
d=[[M]*(1<<K) for _ in range(N+1)]
d[0][0]=0
for i in range(N):
    a=A[i]-1
    for b in range(1<<K):
        d[i+1][b]=min(d[i+1][b],d[i][b]+min(p[b],K-p[b]));c=b|(1<<a)
        if b != c:
            d[i+1][c]=min(d[i+1][c],d[i][b]+p[b>>(a)])
print(d[-1][-1])
