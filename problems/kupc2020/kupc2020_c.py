import random

def solve(n):
    ans = [[0]]
    appeared = set()
    for i in range(1, n):
        for j in range(i):
            k = random.randint(0, 25)
            cnt = 0
            if j == 0:
                while f'{ans[j][-1]}_{k}' in appeared:
                    k = random.randint(0, 25)
                    cnt += 1
                    if cnt >= 100:
                        return
                appeared.add(f'{ans[j][-1]}_{k}')
                ans[j].append(k)
            else:
                while f'{ans[j][-1]}_{k}' in appeared or f'{ans[j-1][-1]}_{k}' in appeared or f'{ans[j][-1]}_{k}' == f'{ans[j-1][-1]}_{k}':
                    k = random.randint(0, 25)
                    cnt += 1
                    if cnt >= 100:
                        return
                appeared.add(f'{ans[j][-1]}_{k}')
                appeared.add(f'{ans[j-1][-1]}_{k}')
                ans[j].append(k)
        tmp = []
        for j in range(i + 1):
            k = random.randint(0, 25)
            cnt = 0
            if len(tmp) == 0:
                while f'{ans[-1][j]}_{k}' in appeared:
                    k = random.randint(0, 25)
                    cnt += 1
                    if cnt >= 100:
                        return
                tmp.append(k)
                appeared.add(f'{ans[-1][j]}_{k}')
            else:
                while f'{ans[-1][j]}_{k}' in appeared or f'{tmp[-1]}_{k}' in appeared or f'{ans[-1][j]}_{k}' == f'{tmp[-1]}_{k}':
                    k = random.randint(0, 25)
                    cnt += 1
                    if cnt >= 100:
                        return
                appeared.add(f'{tmp[-1]}_{k}')
                tmp.append(k)
                appeared.add(f'{ans[-1][j]}_{k}')
        ans.append(tmp)
    return ans

ans = None
while ans is None:
    ans = solve(15)
print(len(ans))
for i in ans:
    print(''.join(map(lambda i: chr(i+97), i)))
