N = int(input())
S = input()
a_pos = []
b_pos = []
for i, s in enumerate(S):
    if s == 'a':
        a_pos.append(i)
    else:
        b_pos.append(i)
S_pos = []
a_i, b_i = 0, 0
for s in S:
    if s == 'a':
        S_pos.append((s, a_i))
        a_i += 1
    elif s == 'b':
        S_pos.append((s, b_i))
        b_i += 1

def get_s(l):
    l = set(l)
    ret = ''
    for s, i in S_pos:
        if i in l:
            ret += s
    return ret

dp = ['']*(N+1) # i以前を採用しない辞書順最大

for i in range(N-1, -1, -1):
    # iを採用する最大を探る
    if a_pos[i] < b_pos[i]:
        j = i+1
        # aa~よりabのがでかいのでそこまでスキップして採用
        while j<N and min(a_pos[j], b_pos[j])<b_pos[i]:
            j += 1
        dp[i] = 'ab'+dp[j]
    else:
        tmp = [i]
        right = a_pos[i]
        j = i+1
        # 手前にbがあればあるだけいいのでb_pos[i]よりも右で右端のaよりも左のbは全て採用する
        while j<N and b_pos[j] < right:
            tmp.append(j)
            right = a_pos[j]
            j+=1
        # 採用するだけしたらそのさきは過去の結果を使う
        while j<N and min(a_pos[j], b_pos[j])<b_pos[i]:
            j += 1
        dp[i] = get_s(tmp)+dp[j]
    if dp[i] < dp[i+1]:
        dp[i] = dp[i+1]
print(dp[0])
