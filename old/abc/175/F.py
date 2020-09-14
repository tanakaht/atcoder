import sys, heapq, math

input = sys.stdin.readline
N = int(input())
SC = []
for _ in range(N):
    S, C = input().split()
    SC.append((S, int(C)))

nodes = dict()
nodes['S'] = []
for s, c in SC:
    for i in range(len(s)+1):
        nodes['L'+s[i:]] = []
        nodes['R'+s[-i::-1]] = []
for node in nodes.keys():
    for s, c in SC:
        if node[0] == 'L':
            if s[::-1].startswith(node[1:]):
                nodes[node].append(('R' + s[-len(node)::-1], c))
            elif node[1:].startswith(s[::-1]):
                nodes[node].append(('L' + node[1 + len(s):], c))
        elif node[0] == 'R':
            if s.startswith(node[1:]):
                nodes[node].append(('L' + s[len(node)-1:], c))
            elif node[1:].startswith(s):
                nodes[node].append(('R' + node[1 + len(s):], c))
for s, c in SC:
    nodes['S'].append(('L' + s, c))
    nodes['S'].append(('R' + s[::-1], c))
nodes['L'] = [('G', 0)]
nodes['R'] = [('G', 0)]
for node in nodes.keys():
    if len(node) != 1 and node[1:]==node[1:][::-1]:
        nodes[node].append(('G', 0))

HQ = [(0, 'S')]
heapq.heapify(HQ)
ans = -1
while len(HQ)>0:
    c, node = heapq.heappop(HQ)
    if node == 'G':
        ans = c
        break
    for node_, c_ in nodes[node]:
        heapq.heappush(HQ, (c+c_, node_))
    nodes[node] = []

print(ans)