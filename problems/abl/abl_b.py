A, B, C, D = map(int, input().split())
ac = max(A, C)
bd = min(B, D)
print('Yes' if bd>=ac else 'No')
