N = int(input())
A = list(map(int, input().split()))
P = int(1e9+7)

suma=0
for a in A:
    suma = (suma + a) % P
ans=0
for a in A:
    suma = (suma - a)%P
    ans = (ans + a * suma) % P
print(ans)
