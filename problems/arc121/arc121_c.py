import sys
import heapq

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))
    ls = [[], []] # oddで選択できる？
    for i, p in enumerate(P):
        i += 1
        if p<i:
            heapq.heappush(ls[(i-1)%2], (p, i))
    cnt = 1
    ans = []
    while len(ls[0])+len(ls[1])>0:
        found = False
        while len(ls[cnt])>0:
            p, i = heapq.heappop(ls[cnt])
            if P[i-1]==p:
                found = True
                break
        if not found:
            piv = 2-cnt
            ans.append(piv)
            P[piv-1], P[piv] = P[piv], P[piv-1]
            cnt ^= 1
            for x in range(2):
                if P[piv+x-1] < piv+x:
                    heapq.heappush(ls[(piv+x-1)%2], (P[piv+x-1], piv+x))
        else:
            for piv in range(i-1, p-1, -1):
                ans.append(piv)
                P[piv-1], P[piv] = P[piv], P[piv-1]
                cnt ^= 1
                for x in range(2):
                    if P[piv+x-1] < piv+x:
                        heapq.heappush(ls[(piv+x-1)%2], (P[piv+x-1], piv+x))
        for i in range(2):
            while len(ls[i])>0:
                p, i_ = ls[i][0]
                if P[i_-1]==p:
                    break
                heapq.heappop(ls[i])
    print(len(ans))
    print(*ans)
