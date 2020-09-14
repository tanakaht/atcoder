from itertools import product

N = int(input())
ab = [tuple(map(int, input().split())) for _ in range(N-1)]
M = int(input())
uv = [tuple(map(int, input().split())) for _ in range(M)]


class Node:
    def __init__(self, nodeid, parent=None):
        self.nodeid = nodeid
        self.parent = parent
        self.children = []

    def add_child(self, nodeid, edgeid):
        child = Node(nodeid, parent=self)
        self.children.append((child, edgeid))

    def parents(self):
        if self.parent == None:
            return [self.nodeid]
        else:
            return [self.nodeid] + self.parent.parents()

    def path(self, to):
        if to == self.nodeid:
            return []
        for child, edgeid in self.children:
            try:
                ret = [edgeid] + child.path(to)
                return ret
            except ValueError:
                pass
        raise ValueError


root = Node(1)
nodes = {1: root}
leef = [root]
while len(leef) > 0:
    node = leef.pop()
    parentid = node.parent and node.parent.nodeid
    for i, (a, b) in enumerate(ab):
        if a == node.nodeid and b != parentid:
            node.add_child(b, i)
            leef.append(node.children[-1][0])
            nodes[b] = node.children[-1][0]
        elif b == node.nodeid and a != parentid:
            node.add_child(a, i)
            leef.append(node.children[-1][0])
            nodes[a] = node.children[-1][0]


constraints = [0]*M

for i, (u, v) in enumerate(uv):
    parents_u = nodes[u].parents()
    for p in nodes[v].parents():
        if p in parents_u:
            break
    for j in nodes[p].path(u):
        constraints[i] += pow(2, j)
    for j in nodes[p].path(v):
        constraints[i] += pow(2, j)

ans = 0
for idx in product([True, False], repeat=M):
    sumidx = sum(idx)
    constraint = 0
    for i, flg in enumerate(idx):
        if flg:
            constraint = constraint | constraints[i]
    C = bin(constraint)[2:].count('1')
    ans += pow(2, N-1-C) * ((-1)**(sumidx%2))

print(ans)
