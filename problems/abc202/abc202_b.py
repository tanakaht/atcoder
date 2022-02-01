S = input()
d = {0: 0, 1: 1, 6: 9, 9: 6, 8:8}
d = {str(k): str(v) for k, v in d.items()}
ans = [d[i] for i in S[::-1]]
print(''.join(ans))
