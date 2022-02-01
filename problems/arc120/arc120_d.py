N = int(input())
A = list(map(int, input().split()))
is_big = [None]*(2*N)
cnt = 0
for i, a in sorted(enumerate(A), key=lambda x: x[1]):
    is_big[i] = cnt>=N
    cnt += 1

cnt = 0
is_big_flg = None # True=>bigが(, smallが)
ans = []
for i in range(2*N):
    if is_big_flg is None:
        is_big_flg = is_big[i]
        ans.append('(')
        cnt = 1
    elif is_big_flg:
        if is_big[i]:
            ans.append('(')
            cnt += 1
        else:
            ans.append(')')
            cnt -= 1
    else:
        if not is_big[i]:
            ans.append('(')
            cnt += 1
        else:
            ans.append(')')
            cnt -= 1
    if cnt == 0:
        is_big_flg = None
print(''.join(ans))
