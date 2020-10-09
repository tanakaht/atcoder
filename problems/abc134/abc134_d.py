N = int(input())
A = list(map(int, input().split()))
B = [0] * N

for i, a in list(enumerate(A))[::-1]:
    i += 1
    d = sum(B[i - 1::i])
    if a != (d % 2):
        B[i - 1] = 1
print(sum(B))
for i, b in enumerate(B):
    if b != 0:
        print(i+1)
