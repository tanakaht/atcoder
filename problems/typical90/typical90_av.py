i=lambda :map(int,input().split())
N,K=i()
v=[];x=v.append
[(x(a-b),x(b)) for a,b in [i() for _ in range(N)]]
print(sum(sorted(v)[-K:]))
