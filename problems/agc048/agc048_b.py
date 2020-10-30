import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
AB_odd, AB_even = [], []
for i, (a, b) in enumerate(zip(A, B)):
    if i % 2 == 0:
        AB_even.append(b - a)
    else:
        AB_odd.append(b - a)
ans = sum(A)
AB_odd = sorted(AB_odd)[::-1]
AB_even = sorted(AB_even)[::-1]
i = 0
while i < len(AB_odd) and i < len(AB_even) and AB_odd[i] + AB_even[i] > 0:
    ans += AB_odd[i] + AB_even[i]
    i += 1
print(ans)
