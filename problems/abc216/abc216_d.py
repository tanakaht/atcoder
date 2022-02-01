import sys

N, M = map(int, input().split())
As = []
for i in range(M):
    k = int(input())
    A = list(map(int, input().split()))[::-1]
    As.append(A)
available = set()
n2idx = {}
q = [i for i in range(M)]
cnt = 0
while q:
    i = q.pop()
    if not As[i]:
        continue
    a = As[i][-1]
    if a in available:
        cnt += 1
        j = n2idx[a]
        available.remove(a)
        As[i].pop()
        As[j].pop()
        q.append(i)
        q.append(j)
    else:
        available.add(a)
        n2idx[a] = i
print('Yes' if cnt==N else 'No')
