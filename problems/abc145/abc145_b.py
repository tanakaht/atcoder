N = int(input())
S = input()
if S == S[:N // 2] + S[:N // 2]:
    print('Yes')
else:
    print('No')
