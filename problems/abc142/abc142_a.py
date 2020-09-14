N = int(input())
cnt = sum([i % 2 for i in range(1, N + 1)])
print(cnt/N)
