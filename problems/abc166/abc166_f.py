import sys

input = sys.stdin.readline
N, A, B, C = map(int, input().split())
s = [input().rstrip() for _ in range(N)]

ans = []
if A+B+C >= 2:
    if sum([i != 0 for i in [A, B, C]]) == 1 and ((A != 0 and s[0] == 'BC') or (B != 0 and s[0] == 'AC') or (C != 0 and s[0] == 'AB')):
        print('No')
        sys.exit()
    for i in range(N):
        if s[i] == 'AB':
            if A == 0:
                ans.append('A')
                A += 1
                B -= 1
            elif A == 1 and B != 0 and i != N - 1 and s[i + 1] == 'AC':
                ans.append('A')
                A += 1
                B -= 1
            else:
                ans.append('B')
                A -= 1
                B += 1
        elif s[i] == 'BC':
            if B == 0:
                ans.append('B')
                B += 1
                C -= 1
            elif B == 1 and C != 0 and i != N-1 and s[i+1] == 'AB':
                ans.append('B')
                B += 1
                C -= 1
            else:
                ans.append('C')
                B -= 1
                C += 1
        elif s[i] == 'AC':
            if A == 0:
                ans.append('A')
                A += 1
                C -= 1
            elif A == 1 and C != 0 and i != N-1 and s[i+1] == 'AB':
                ans.append('A')
                A += 1
                C -= 1
            else:
                ans.append('C')
                A -= 1
                C += 1
        if A < 0 or B < 0 or C < 0:
            print(ans)
            raise ValueError('nannkahenn')
else:
    for i in range(N):
        if s[i] == 'AB':
            if A == 0:
                ans.append('A')
                A += 1
                B -= 1
            else:
                ans.append('B')
                A -= 1
                B += 1
        elif s[i] == 'BC':
            if B == 0:
                ans.append('B')
                B += 1
                C -= 1
            else:
                ans.append('C')
                B -= 1
                C += 1
        elif s[i] == 'AC':
            if A == 0:
                ans.append('A')
                A += 1
                C -= 1
            else:
                ans.append('C')
                A -= 1
                C += 1
        if A < 0 or B < 0 or C < 0:
            print('No')
            sys.exit()

print('Yes')
for i in ans:
    print(i)
