import sys, math

# input = sys.stdin.readline

H, W = map(int, input().split())
Ch, Cw = map(int, input().split())
Dh, Dw = map(int, input().split())
S = [[1 if s=='.' else 0 for s in input()] for _ in range(H)]
costs = [[math.inf]*W for _ in range(H)]
costs[Ch-1][Cw-1] = 0
que = [(0, Ch-1, Cw-1)]
next_que = []

while len(next_que)>0 or len(que)>0:
    while len(que)>0:
        c, h, w = que.pop(0)
        if c >= costs[Dh-1][Dw-1]:
            print(costs[Dh-1][Dw-1])
            sys.exit()
        for i, j in [(h-1, w), (h+1, w), (h, w-1), (h, w+1)]:
            if i < 0 or j < 0 or i>=H or j>=W:
                continue
            if i == Dh - 1 and j == Dw - 1:
                print(c)
                sys.exit()
            if S[i][j] and costs[i][j] > c:
                costs[i][j] = c
                que.append((c, i, j))
        for dw in [-2, -1, 0, 1, 2]:
            for dh in [-2, -1, 0, 1, 2]:
                if w+dw < 0 or h+dh < 0 or w+dw>=W or h+dh>=H:
                    continue
                if S[h+dh][w+dw] and costs[h+dh][w+dw] > c+1:
                    costs[h+dh][w+dw] = c+1
                    next_que.append((c+1, h+dh, w+dw))
    que = next_que
    next_que = []

print(-1)
