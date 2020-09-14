N = int(input())
C = input()

r_cnt = 0
for c in C:
    r_cnt += c=='R'
ans = 0
for c in C[:r_cnt]:
    ans += c=='W'
print(ans)
