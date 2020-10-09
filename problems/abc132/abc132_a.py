from collections import Counter
import sys

S = input()
c = Counter(S)
for k, v in c.items():
    if v != 2:
        print('No')
        sys.exit(0)
print('Yes')
