import sys
import time

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        d = {root: [] for root in self.roots()}
        for i in range(self.n):
            d[self.find(i)].append(i)
        return d

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

input = sys.stdin.readline
ts = time.time()
si, sj = map(int, input().split())
N = 50
T = [list(map(int, input().split()))+[N*N] for _ in range(N)]
P = [list(map(int, input().split()))+[N*N] for _ in range(N)]
dir_d = {'U': (-1, 0), 'L': (0, -1), 'D':(1, 0), 'R':(0, 1)}

# state=使ったタイルで、xs, ysからいける特典
def cal_possible_score(state, xs, ys):
    uf = UnionFind(N*N)
    for x in range(N):
        for y in range(N):
            if (not (x==xs and y==ys)) and state[T[x][y]]:
                continue
            for d in 'LRUD':
                dx, dy = dir_d[d]
                x_, y_ = x+dx, y+dy
                if not (0<=x_<N and 0<=y_<N):
                    continue
                if (not state[T[x_][y_]]) and T[x_][y_]!=T[x][y]:
                    uf.union(x+y*N, x_+y_*N)
    points = [0]*(N*N)
    points[T[xs][ys]] = P[xs][ys]
    ret = 0
    for i in uf.members(xs+ys*N):
        x, y = i%N, i//N
        tile_id = T[x][y]
        if points[tile_id] < P[x][y]:
            ret += 5
            points[tile_id] = N*N
            #ret += P[x][y] - points[tile_id]
            #points[tile_id] = P[x][y]
    return ret

# state=score, tile_state, x, y
def beam_search(seed_states, n=5, cal_score=cal_possible_score):
    new_seeds = []
    appeard_roots = set([s[-1] for s in seed_states])
    for seed_state in seed_states:
        score_for_search, score_getted, tile_state, xs, ys, root = seed_state
        for d in 'LRUD':
            dx, dy = dir_d[d]
            x_, y_ = xs+dx, ys+dy
            if not (0<=x_<N and 0<=y_<N):
                continue
            if tile_state[T[x_][y_]]:
                continue
            root_ = root+d
            if root_ in appeard_roots:
                continue
            tile_state_ = [t for t in tile_state]
            tile_state_[T[x_][y_]] = 1
            score_getted_ = score_getted+P[x_][y_]
            score_for_search_ = 2*score_getted_ + cal_score(tile_state_, x_, y_)
            new_seeds.append((score_for_search_, score_getted_, tile_state_, x_, y_, root_))
    # new_seeds = sorted(new_seeds+seed_states[:2])[::-1]
    # flg = not (len(seed_states)==n and new_seeds[n-1][0]==seed_states[n-1][0])
    new_seeds = sorted(new_seeds)[::-1]
    flg = True
    return flg, new_seeds[:n]

tile_state = [0]*(N*N)
tile_state[T[si][sj]]
seed_states = [(0, 0, tile_state, si, sj, '')]
flg = True
while time.time()-ts < 0 and flg:
    flg, new_seed = beam_search(seed_states)
    if len(new_seed) == 0:
        break
    seed_states = new_seed
for i in seed_states:
    print(i[-1])
    print(i[0], i[1])

new_seed = []
for i in seed_states:
    new_seed.append((i[1], i[1], i[2], i[3], i[4], i[5]))
seed_states = new_seed
while time.time()-ts < 3.0 and flg:
    flg, new_seed = beam_search(seed_states, n=200, cal_score=lambda *x: 0)
    if len(new_seed) == 0:
        break
    seed_states = new_seed


for i in seed_states:
    print(i[-1])
    print(i[0], i[1])
