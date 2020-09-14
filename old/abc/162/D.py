N = int(input())
S = input()

color_cnt = {'R': 0, 'G': 0, 'B': 0}
for i in range(N):
    color_cnt[S[i]] += 1

ans = color_cnt['R']*color_cnt['G']*color_cnt['B']
for i in range(N):
    for diff in range(1, (N-i-1)//2 +1):
        ans -= len({S[i], S[i+diff], S[i+2*diff]}) == 3

print(ans)


