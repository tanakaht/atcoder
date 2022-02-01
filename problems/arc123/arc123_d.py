import sys, math
N = int(input())
A = list(map(int, input().split()))
ans_base = sum([abs(a) for a in A])

b, c = A[0], 0
events = []
events.append(min(b, c))
events.append(max(b, c))
for a in A[1:]:
    if b+c<a:
        b = a-c
    else:
        c = a-b
    events.append(c)
    events.append(-b)
ans_ = math.inf
events = sorted(events)
for i in range(10):
    try:
        x = events[len(events)//2-5+i]
    except IndexError:
        continue
    b, c = A[0]+x, -x
    ans = abs(b)+abs(c)
    for a in A[1:]:
        if b+c<a:
            b = a-c
        else:
            c = a-b
        ans += abs(b)+abs(c)
    ans_ = min(ans, ans_)
print(ans_)
