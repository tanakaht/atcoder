S = input()
ans = 0
for i in range(len(S)):
    ans += S[i:i+4]=='ZONe'
print(ans)
