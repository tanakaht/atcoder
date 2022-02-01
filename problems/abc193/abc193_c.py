N = int(input())
ans = N
appeared = set()
for i in range(2, N):
    tmp = i*i
    if tmp > N:
        break
    if i in appeared:
        continue
    for j in range(2, N):
        appeared.add(tmp)
        tmp *= i
        if tmp > N:
            break
    j -= 1
    ans -= max(0, j)
print(ans)
