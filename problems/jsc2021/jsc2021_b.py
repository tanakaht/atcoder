N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(*sorted((A-B).union(B-A)))