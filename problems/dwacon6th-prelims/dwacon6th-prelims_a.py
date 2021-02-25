N = int(input())
S, T = [], []
for _ in range(N):
    s, t = input().split()
    S.append(s)
    T.append(int(t))
X = input()
i = 0
while S[i] != X:
    i += 1
print(sum(T[i+1:]))
