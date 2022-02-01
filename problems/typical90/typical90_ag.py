a,b=map(int ,input().split())
if min(a,b)==1:
    print(max(a, b))
else:
    print(((a+1)//2)*((b+1)//2))
