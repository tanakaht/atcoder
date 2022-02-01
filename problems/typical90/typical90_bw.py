import math
N = int(input())
cnt = 0
for i in range(2, int(math.sqrt(N))+1):
    while N%i==0:
        N//=i
        cnt += 1
cnt += N!=1
print((cnt-1).bit_length())
