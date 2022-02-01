S = input()
N = len(S)
cnts = [0]*N
cnt = 0
for i in range(N):
    if S[i] == '(':
        cnt += 1
        cnts[i] = cnt
    elif S[i] == ')':
        cnt -= 1
        cnts[i] = cnt
    elif S[i] == 'o':
        cnts[i] = cnt
    elif S[i] == 'x':
        cnts[i] = cnt-1


ans = 0
# '('の移動
for i in range(N):
    if cnts[i] < 0:
        tmp1 = 10000000
        for j in range(i+1, N):
            if S[j] == '(':
                tmp1 = j
                break
        tmp2 = -10000000
        for j in range(i):
            if S[j] == ')':
                tmp2 = j
                break
        if tmp1-i<i-tmp2:
            j = tmp1
            for k in range(j, i-1, -1):
                cnts[k] = cnts[k-1]+1
                ans += 1
            cnts[i] += (i>0 and S[i-1]=='x')
            ans -= 1
            S = S[:i]+'('+S[i:j]+S[j+1:]
        else:
            j = tmp2
            for k in range(j, i):
                cnts[k] = cnts[k+1]+1
                ans += 1
            cnts[i] =  cnts[i-1]-1
            S = S[:j]+S[j+1:i]+')'+S[i:]
            break
        print(S)

print(ans)
