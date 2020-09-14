S = input()
S1 = S[:len(S) // 2]
S2 = S[-1:(len(S)-1) // 2:-1]
ans = 0
for s1, s2 in zip(S1, S2):
    ans += s1!=s2
print(ans)
