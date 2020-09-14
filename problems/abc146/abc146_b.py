N = int(input())
S = input()
ans = ''
for s in S:
    i = ord(s)+N
    if i >= 65 + 26:
        i -= 26
    ans += chr(i)
print(ans)
