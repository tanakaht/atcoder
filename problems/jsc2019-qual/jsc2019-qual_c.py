N = int(input())
S = list(map(lambda x: x=='W', input()))
P = int(1e9+7)
rest = 0
ans = 1
for i in range(2*N):
    if S[i]^((i+1)%2):
        rest += 1
    else:
        ans = (ans*rest)%P
        rest -= 1
for i in range(1, N+1):
    ans = (ans*i)%P
ans = ans * (rest==0)
print(ans)
