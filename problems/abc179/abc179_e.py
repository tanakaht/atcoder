N, X, M = map(int, input().split())
ans = 0
loop = 1
def f(a):
    return (a * a) % M


appear = [0] * (M + 1)
tmp = f(X)
appear[X] = loop
while appear[tmp] == 0:
    loop += 1
    appear[tmp] = loop
    tmp = f(tmp)

loopstart = tmp
tmp = X
before_loop_sum = 0
before_loop_len = 0
while tmp != loopstart:
    before_loop_sum += tmp
    before_loop_len += 1
    tmp = f(tmp)

loop_sum = loopstart
loop_len = 1
tmp = f(loopstart)
while tmp != loopstart:
    loop_sum += tmp
    loop_len += 1
    tmp = f(tmp)

if N < before_loop_len:
    tmp = X
    ans = 0
    for i in range(N):
        ans += tmp
        tmp = f(tmp)
else:
    N -= before_loop_len
    ans += before_loop_sum
    n_loop = N // loop_len
    N -= loop_len * n_loop
    ans += n_loop * loop_sum
    tmp = loopstart
    for i in range(N):
        ans += tmp
        tmp = f(tmp)
print(ans)
