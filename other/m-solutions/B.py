a, b, c = map(int, input().split())
k = int(input())
cnt = 0
while a>=b:
    b *= 2
    cnt += 1
while b>=c:
    c *= 2
    cnt += 1

print('Yes' if cnt <= k else 'No')