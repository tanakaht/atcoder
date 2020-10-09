from collections import Counter

n = int(input())
v = list(map(int, input().split()))
c_even = sorted(list(Counter(v[::2]).items()) +
                [(-1, 0)], key=lambda x: x[1])[::-1]
c_odd = sorted(list(Counter(v[1::2]).items()) +
               [(-1, 0)], key=lambda x: x[1])[::-1]
if c_even[0][0] == c_odd[0][0]:
    ans = n - max(c_even[0][1]+c_odd[1][1], c_even[1][1]+c_odd[0][1])
else:
    ans = n - (c_even[0][1] + c_odd[0][1])
print(ans)
