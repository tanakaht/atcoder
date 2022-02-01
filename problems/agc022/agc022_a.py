import sys

S = input()
alphas = set(S)
if len(S) == 26:
    appeared = set()
    max_ = S[-1]
    for i in range(1, len(S)+1):
        if S[-i] < max_:
            min_ = max_
            for s in appeared:
                if s > S[-i]:
                    min_ = min(s, min_)
            print(S[:-i]+min_)
            sys.exit(0)
        max_ = max(max_, S[-i])
        appeared.add(S[-i])
    print(-1)

else:
    for i in range(97, 123):
        if chr(i) not in alphas:
            break
    print(S+chr(i))
