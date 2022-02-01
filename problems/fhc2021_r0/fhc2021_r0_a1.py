import math
from collections import Counter

T = int(input())
vowels = set("AIUEO")
for i in range(T):
    S = input()
    ans = math.inf
    C = Counter(S)
    for c in [chr(i) for i in range(65, 91)]:
        tmp = 0
        for k, v in C.items():
            if k==c:
                continue
            else:
                tmp += v*(2-((k in vowels)^(c in vowels)))
        ans = min(ans, tmp)
    print(f"Case #{i+1}: {ans}")
