import sys
N = int(input())
if N==3:
    print(2,5,63)
    sys.exit(0)
ans = set()
n = 2
while n <= 30000 and N-3 > len(ans):
    if n%6!=0:
        ans.add(n)
    n += 2
rest = (-sum(ans))%6
if rest!=0:
    for i in range(2, 30001, 2):
        if (i%6==rest) and (i not in ans):
            ans.add(i)
            break

n = 3
while n <= 30000 and N-1 > len(ans):
    if n%6!=0:
        ans.add(n)
    n += 3
rest = (-sum(ans))%6
if rest != 0:
    for i in range(3, 30001, 3):
        if (i%6==rest) and (i not in ans):
            ans.add(i)
            break
n = 6
while n <= 30000 and N > len(ans):
    ans.add(n)
    n += 6
print(*ans)
