import sys

N, K = map(int, input().split())
MOD = int(1e5)
# 遷移を定義
def transition(x):
    ret = x
    for i in range(5):
        ret += (x//(10**i))%10
    return ret % MOD

# start から初めてloopの始まる値を見つける
appear = [False] * (int(1e5))
tmp = N
while appear[tmp] == 0:
    appear[tmp] = True
    tmp = transition(tmp)
loop_start = tmp

# start からloop_start までの値を集計
tmp = N
before_loop_len = 0
while tmp != loop_start:
    before_loop_len += 1
    tmp = transition(tmp)
# loop_startから初めてloop_startをもう一度訪れるまでの値を集計
loop_len = 1
tmp = transition(loop_start)
while tmp != loop_start:
    loop_len += 1
    tmp = transition(tmp)

ans = 0
# Nがbefore_loop_len未満 = >for文で回して終わり
if K < before_loop_len:
    tmp = N
    for i in range(K):
        tmp = transition(tmp)
    ans = tmp
else:
    K -= before_loop_len
    # loopを回せるだけ回す
    n_loop = K // loop_len
    K -= loop_len * n_loop
    # あまりをfor文回す
    tmp = loop_start
    for i in range(K):
        tmp = transition(tmp)
    ans = tmp
print(ans)
