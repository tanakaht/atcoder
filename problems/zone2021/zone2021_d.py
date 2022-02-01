from collections import deque
S = input()
T = deque([])
is_rev = False
for s in S:
    if s == 'R':
        is_rev ^= 1
    else:
        if is_rev:
            T.appendleft(s)
        else:
            T.append(s)
if is_rev:
    T = list(T)[::-1]
ans = [None]
for t in T:
    if t == ans[-1]:
        ans.pop()
    else:
        ans.append(t)
print(''.join(ans[1:]))
