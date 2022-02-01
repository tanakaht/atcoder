N = int(input())
ST = sorted([input().split() for _ in range(N)], key=lambda x: int(x[1]))
print(ST[-2][0])
