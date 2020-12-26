N = int(input())
X = list(map(int, input().split()))
mid_l, mid_r = sorted(X)[N//2-1:N//2+1]
for i in range(N):
    if X[i] <= mid_l:
        print(mid_r)
    else:
        print(mid_l)
