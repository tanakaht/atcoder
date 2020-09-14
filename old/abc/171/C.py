import sys
input = sys.stdin.readline

N = int(input())

piv = 0
while True:
    if 26*(26**piv-1)/25 >= N:
        break
    piv += 1
N -= 26*(26**(piv-1)-1)/25 + 1
for i in reversed(range(piv)):
    x = int(N//(26**i)%26)
    print(chr(x+97), end='')
print()
