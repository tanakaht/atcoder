s = input()
K = int(input())
substrings = []
for i in range(len(s)):
    for j in range(i + 1, i + K + 1):
        substrings.append(s[i:j])
substrings = sorted(substrings)
cnt = 0
pre = None
for substring in substrings:
    cnt += substring != pre
    if cnt == K:
        break
    pre = substring
print(substring)
