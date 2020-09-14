s = input()
t = input()
next_alpha = [[-1] * len(s) for _ in range(30)] # (文字種a, 今いるsのインデックス)=>(次のaが出るsのインデックス)
for i, s_ in enumerate(s):
    j = ord(s_) - 97
    for k in range(i, -1, -1):
        if next_alpha[j][k] != -1:
            break
        next_alpha[j][k] = i

ans = 0
for t_ in t:
    i = ans % len(s)
    tmp = next_alpha[ord(t_) - 97][i]
    if tmp == -1:
        ans += (-1 * ans) % len(s)
        i = ans % len(s)
        tmp = next_alpha[ord(t_) - 97][i]
    if tmp == -1:
        ans = -1
        break
    else:
        ans += tmp - (i - 1)
print(ans)
