# maspy

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
m = map(int, read().split())
AB = zip(m, m)

MOD = 10 ** 9 + 7

graph = [[] for _ in range(N+1)]
for a, b in AB:
    graph[a].append(b)
    graph[b].append(a)

root = 1
parent = [0] * (N+1)
order = []
stack = [root]
while stack:
    x = stack.pop()
    order.append(x)
    for y in graph[x]:
        if y == parent[x]:
            continue
        parent[y] = x
        stack.append(y)

# (1/2)^n
x = (MOD + 1) // 2
power = [1] * (N+100)
power_inv = [1] * (N+100)
for i in range(1, N+100):
    power[i] = power[i-1] * 2 % MOD
    power_inv[i] = power_inv[i-1] * x % MOD

# 部分木の大きさ
answer = 0
size = [1] * (N+1)
for v in order[::-1]:
    p = parent[v]
    size[p] += size[v]
    A = [size[w] for w in graph[v] if w != p]  # 部分木のサイズ集合
    if v != root:
        A.append(N - 1 - sum(A))
    if len(A) == 1:
        continue
    prod = 1
    coef = 1
    for x in A:
        prod *= power_inv[x]
        prod %= MOD
        coef += (power[x] - 1)
    E = 1 - prod * coef % MOD
    answer += E

answer *= power_inv[1]
answer %= MOD
print(answer)
