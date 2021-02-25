"""
感想

- 期待値*全パターン数なのでありうるパターン全てで移動距離を足し合わせれば良い
- 数式たててこねて総和の撮り方を帰るパターンだなあ
- x[i]からx[j]へと移動するパターンを数える
- x[j]からx[j-1]について全パターンで何回この区間を通るかに言い換え(=>上のiについて足し合わせる)=>(N-1)!/(j-i)になる
- 数式こねて終わり
"""

N = int(input())
X = list(map(int, input().split()))
P = int(1e9+7)
ans = 0
tyouwa_kyusuu = [0]
for i in range(1, N+2):
    tyouwa_kyusuu.append((tyouwa_kyusuu[-1]+pow(i, P-2, P))%P)
for i in range(1, N):
    ans = (ans + (X[i]-X[i-1])*tyouwa_kyusuu[i])%P
for i in range(1, N):
    ans = (ans*i)%P
print(ans)
