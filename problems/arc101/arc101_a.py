import math

N, K = map(int, input().split())
x = list(map(int, input().split()))
x_pos = sorted([0]+[i for i in x if i >= 0])
x_neg = sorted([0]+[(-1)*i for i in x if i < 0])
ans = math.inf
for i in range(K + 1):
    try:
        ans = min(ans, x_pos[i] + x_neg[K - i] +
                  min(x_pos[i], x_neg[K - i]))
    except IndexError:
        pass
print(ans)
