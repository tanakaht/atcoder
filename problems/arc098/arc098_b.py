N = int(input())
A = list(map(int, input().split()))
right = 0
ans = 0
xor = 0
for left in range(N):
    while right<N and xor & A[right] == 0:
        xor = xor ^ A[right]
        right += 1
    ans += right - left
    xor = xor^A[left]
print(ans)
