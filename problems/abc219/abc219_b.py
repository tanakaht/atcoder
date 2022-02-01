import sys

S = [input() for _ in range(3)]
T = input()
print(''.join([S[int(i)-1] for i in T]))
