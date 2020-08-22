import sys, math

input = sys.stdin.readline
N = int(input())
scores = []
for _ in range(N):
    a, b = map(int, input().split())
    flg = 0
    if b == 0:
        score = 0
        flg = 1
    else:
        score = a/b
        if score<0:
            score = -1/score
            flg = 1
    scores.append((score, flg))

scores = sorted(scores)
ans = 1
pre = -1
pre_cnt = [0, 0]
for i, (score, flg) in enumerate(scores):
    if pre==score:
        rate = (2**pre_cnt[flg])/(2**pre_cnt[0]+2**pre_cnt[1]-1)
        ans += int(ans*rate)
        pre_cnt[flg] += 1
    else:
        ans += ans
        pre = score
        pre_cnt = [0, 0]
        pre_cnt[flg] += 1

print((ans-1)%1000000007)