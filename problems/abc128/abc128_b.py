N = int(input())
SP = []
for i in range(N):
    s, p = input().split()
    p = int(p)
    SP.append((i + 1, s, p))
SP = sorted(SP, key=lambda x: x[2])[::-1]
SP = sorted(SP, key=lambda x: x[1])
for i, _, _ in SP:
    print(i)
