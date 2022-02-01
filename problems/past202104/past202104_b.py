S = input()
Ss = [S[4*i:4*i+4] for i in range(len(S)//4)]
ans = 'none'
for i, s in enumerate(Ss):
    if s=='post':
        ans = i+1
print(ans)
