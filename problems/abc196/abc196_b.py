S = input()
ans = ''
for s in S:
    if s == '.':
        break
    ans += s
print(int(ans))
