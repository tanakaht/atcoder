A, B, X = map(int, input().split())
keta = 0
while (keta+1) * B + A * pow(10, keta) <= X:
    keta += 1
X -= (keta) * B
ans = min(X // A, pow(10, keta)-1)
print(min(ans, pow(10, 9)))
