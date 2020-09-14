N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

pre = -1
ans = 0
for a in A:
    ans += B[a - 1]
    if a == pre + 1:
        ans += C[pre - 1]
    pre = a
print(ans)
