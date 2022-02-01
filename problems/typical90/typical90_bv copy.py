"""
a, b, c →　0, 1, 2 (mod3)とする
操作: Si!=0(mod3)なiを選択
- Si -= 1
- Sj += 1 (j<i)
と言い換えられる
仮想的にS0を入れると
\Sigma_i{Si*2^(i-1)}+S0
が保存されている
左はじから貪欲にやり続けるとSi=0(i>=1)とできる.

とするとN=10^5で溶けるんですごい嘘っぽいけど出してみる
貪欲実際にやると
"""

N = int(input())
S = input()
d = {'a': 0, 'b': 1, 'c': 2}
ans = 0
tmp = 1
for s in S:
    ans += d[s]*tmp
    tmp *= 2
print(ans)
