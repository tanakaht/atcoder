p=[0]*5001
for d,c,s in sorted([list(map(int,input().split())) for _ in range(int(input()))]):
  for j in range(d,c-1,-1):
    p[j]=max(p[j], p[j-c]+s)
print(max(p))
