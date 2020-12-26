N = int(input())
A = [0]+list(map(int, input().split()))+[0]
cost_base = 0
pre = 0
for a in A:
    cost_base += abs(a-pre)
    pre = a

for i in range(1, N+1):
    ans = cost_base
    ans -= abs(A[i]-A[i-1]) + abs(A[i]-A[i+1])
    ans += abs(A[i+1]-A[i-1])
    print(ans)
