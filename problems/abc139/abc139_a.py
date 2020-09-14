S = input()
T = input()
cnt = 0
for s, t in zip(S, T):
    cnt += s == t
print(cnt)
