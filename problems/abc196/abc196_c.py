N = int(input())
i = 1
ans = 0
while True:
    if int(str(i) + str(i)) > N:
        break
    i += 1
    ans += 1
print(ans)
