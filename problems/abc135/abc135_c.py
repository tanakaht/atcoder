N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0
for i in range(N):
    b = B[i]
    if B[i] <= A[i]:
        cnt += B[i]
    elif B[i] <= A[i] + A[i + 1]:
        cnt += B[i]
        A[i + 1] -= B[i] - A[i]
    else:
        cnt += A[i] + A[i + 1]
        A[i+1] = 0
print(cnt)
