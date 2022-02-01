N = int(input())
A = sorted(list(map(int, input().split())))[::-1]
P = int(1e9)+7
ans = 1
for i in range(N-1):
    ans = (ans*(A[i]-A[i+1]+1))%P
ans = (ans*(A[-1]+1))%P
print(ans)
