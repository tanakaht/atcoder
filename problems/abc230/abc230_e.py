import math

N = int(input())
ans = 0
# [i/N]=x毎に集計
i = 1
while i<=N:
    x = N//i
    j = N//x
    ans += x*(j-i+1)
    i = j+1
print(ans)
