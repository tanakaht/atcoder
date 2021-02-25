import sys
N = int(input())
print(pow(2, N)-1)
for i in range(1, pow(2, N)):
    for j in range(pow(2, N)):
        if bin(i&j)[2:].count('1')%2==0:
            print('A', end='')
        else:
            print('B', end='')
    print()
