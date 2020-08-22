N = int(input())
A = list(map(int, input().split()))
money = 1000
kabu = 0
for i in range(N):
    if i==N-1 or A[i] > A[i+1]:
        money += kabu*A[i]
        kabu = 0
    elif A[i] < A[i+1]:
        kabu += money//A[i]
        money %= A[i]
print(money)