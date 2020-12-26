N = int(input())
A = list(map(int, input().split()))
ans = 0
for a in A:
  while a%6 in [0, 2, 4, 5]:
    a -= 1
    ans += 1
print(ans)
