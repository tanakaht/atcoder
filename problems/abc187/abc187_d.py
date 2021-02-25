
N = int(input())
AB = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: 2*x[0]+x[1])[::-1]
taka = 0
ao = sum(map(lambda x: x[0], AB))
ans = 0
i = 0
while taka<=ao:
    ans += 1
    ao -= AB[i][0]
    taka += sum(AB[i])
    i += 1
print(ans)
