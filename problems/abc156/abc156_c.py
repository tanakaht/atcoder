N = int(input())
X = list(map(int, input().split()))

costs = [0] * 100
for x in X:
    for i in range(100):
        costs[i] += (x - (i + 1)) * (x - (i + 1))
print(min(costs))
