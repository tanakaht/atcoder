from collections import Counter
import sys
S = input()
if len(S) == 1:
    if int(S) % 8 == 0:
        print('Yes')
    else:
        print('No')
    sys.exit(0)
elif len(S) == 2:
    if (int(S[0])*10+int(S[1])) % 8 == 0 or (int(S[1])*10+int(S[0])) % 8 == 0:
        print('Yes')
    else:
        print('No')
    sys.exit(0)


C = Counter(map(int, S))

for i in C.keys():
    for j in C.keys():
        for k in C.keys():
            C_tmp = Counter([i, j, k])
            is_evil = False
            for k_, v in C_tmp.items():
                is_evil = is_evil or C[k_] < v
            if is_evil:
                continue
            if (100 * i + 10 * j + k) % 8 == 0:
                print('Yes')
                sys.exit(0)
print('No')
