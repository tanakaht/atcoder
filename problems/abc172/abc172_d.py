N = int(input())
ans = 0
for i in range(1, N+1):
    til = N//i
    divsum = int(til*(til+1)/2)
    ans += divsum*i
print(ans)
