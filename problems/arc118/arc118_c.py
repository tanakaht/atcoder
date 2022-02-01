import math

N = int(input())
# 高速素因数分解
divs = [-1]*(10000+1)
divs[1] = 1
for i in range(2, 10000+1):
    if divs[i] == -1:
        for j in range(1, 10000//i+1):
            divs[i*j] = i

sosuu = []
base = 1
cnt = 0
for i in range(2, 10000+1):
    if 3*i>10000:
        break
    if divs[i] == i:
        base *= i
        sosuu.append(i)

ans = [6, 10, 15]
x = 2
while len(ans)<N and x*6<10000:
    ans.append(x*6)
    x += 1
x = 2
while len(ans)<N and x*10<10000:
    if x%3==0:
        x += 1
        continue
    ans.append(x*10)
    x += 1

x = 2
while len(ans)<N and x*15<10000:
    if x%2==0:
        x += 1
        continue
    ans.append(x*15)
    x += 1


print(*ans)

for a in ans:
    assert a<= 10000
for i in range(N):
    for j in range(i+1, N):
        assert math.gcd(ans[i], ans[j])>1

gcd_ = ans[0]
for i in range(1,N):
    gcd_ = math.gcd(gcd_, ans[i])
assert gcd_ == 1
