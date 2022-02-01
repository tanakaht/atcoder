from collections import defaultdict
c2idx = {c: i for i, c in enumerate("KEY")}
S = list(map(lambda x: c2idx[x], input()))
K = int(input())
cnts = [[[0, 0, 0]] for _ in range(3)] # 1-idxed
cnt = [0, 0, 0]
for s in S:
    cnt[s] += 1
    cnts[s].append(tuple(cnt))
final_cnt = cnt
dp = defaultdict(int) # (交差数, *cnt)->種類の数
dp[0, 0, 0, 0] = 1
for _ in range(len(S)):
    dp_new = defaultdict(int)
    for (kousa, *cnt), n in dp.items():
        for i in range(3):
            if cnt[i]+1<=final_cnt[i]:
                cnt_ = list(cnt)
                cnt_[i] += 1
                kousa_ = kousa+sum([max(0, c1-c2) for c1, c2 in zip(cnt_, cnts[i][cnt_[i]])])
                dp_new[kousa_, cnt_[0], cnt_[1], cnt_[2]] += n
    dp = dp_new
ans = 0
for (kousa, *cnt), n in dp.items():
    ans += (kousa<=K)*n
print(ans)
