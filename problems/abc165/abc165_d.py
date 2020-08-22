A, B, N = map(int, input().split())
x = N if N<B else B-1

ans = int(A*x/B)-A*int(x/B)
print(ans)

