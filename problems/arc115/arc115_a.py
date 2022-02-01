import sys
N, M = map(int, input().split())
S = [input() for _ in range(N)]
# 同じ可能性がある/ない<=>回答の不一致数が偶数/奇数
# 同じ可能性があるは推移律
# 0..00と0..01と成り立つかで2つに分けれる
# それら同士は同じ可能性がない
odds, evens = 0, 0
for s in S:
    if s.count("1")%2:
        odds += 1
    else:
        evens += 1
print(odds*evens)
