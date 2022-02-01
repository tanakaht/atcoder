import sys
import math
from logging import LogRecord, getLogger, StreamHandler, FileHandler, DEBUG
logger = getLogger(__name__)    #以降、このファイルでログが出たということがはっきりする。
handler = FileHandler("./log.txt")
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)


def cos_sim(A, B, div_norm=True):
    eps = 1e-7
    ret = 0
    norm_a, norm_b = 0, 0
    for a, b in zip(A, B):
        ret += a*b
        norm_a += a*a
        norm_b += b*b
    if div_norm:
        return ret/(math.sqrt(norm_a)*math.sqrt(norm_b)+eps)
    else:
        return ret


N, M, K, R = list(map(int, input().split()))
tasks__ = [list(map(int, input().split())) for _ in range(N)]
UV = [list(map(int, input().split())) for _ in range(R)]
g = [[] for _ in range(N)]
g_inv = [[] for _ in range(N)]
for u, v in UV:
    u -= 1
    v -= 1
    g[u].append(v)
    g_inv[v].append(u)
# S = [[0, 7, 28, 1, 11, 10, 9, 7, 4, 1, 6, 4, 2, 12, 9], [16, 1, 14, 9, 0, 5, 15, 6, 2, 0, 4, 6, 2, 4, 7], [3, 3, 3, 1, 5, 12, 25, 2, 7, 13, 4, 20, 12, 23, 6], [13, 11, 6, 3, 11, 27, 3, 9, 8, 5, 10, 4, 2, 2, 16], [6, 5, 2, 1, 6, 14, 2, 15, 14, 3, 20, 6, 5, 17, 0], [3, 13, 18, 26, 22, 14, 14, 0, 10, 0, 16, 10, 17, 5, 8], [18, 11, 8, 7, 7, 9, 15, 12, 28, 4, 4, 1, 0, 3, 8], [1, 1, 4, 5, 9, 2, 5, 12, 5, 2, 7, 3, 3, 3, 2], [6, 11, 0, 6, 5, 5, 8, 0, 18, 5, 8, 0, 7, 5, 5], [19, 19, 6, 16, 9, 20, 13, 5, 14, 16, 9, 16, 5, 2, 12], [8, 7, 4, 6, 14, 14, 3, 8, 3, 3, 27, 4, 6, 11, 10], [1, 1, 0, 7, 1, 11, 8, 7, 22, 5, 18, 7, 10, 12, 21], [12, 13, 1, 12, 13, 5, 25, 23, 22, 9, 23, 8, 3, 14, 21], [3, 2, 14, 6, 15, 9, 3, 1, 16, 6, 7, 1, 6, 1, 1], [1, 0, 7, 12, 1, 2, 0, 1, 2, 6, 4, 1, 14, 6, 16], [0, 9, 4, 4, 1, 6, 7, 5, 1, 8, 14, 5, 15, 1, 1], [2, 11, 9, 12, 11, 3, 4, 19, 5, 4, 9, 4, 18, 30, 27], [8, 5, 1, 3, 26, 24, 7, 5, 5, 5, 18, 7, 15, 6, 2], [5, 4, 1, 3, 3, 9, 0, 4, 1, 11, 4, 6, 10, 6, 6], [8, 14, 12, 4, 14, 2, 3, 7, 6, 23, 18, 8, 7, 2, 11]]
# S = [[0, 1, 5, 11, 2, 0, 9, 8, 12, 1, 13, 29, 9, 23, 6, 1, 8], [4, 15, 2, 11, 2, 12, 1, 3, 10, 1, 6, 11, 10, 2, 10, 10, 3], [5, 11, 14, 8, 2, 5, 18, 10, 14, 13, 5, 4, 20, 19, 9, 2, 19], [1, 4, 12, 6, 6, 4, 7, 8, 3, 5, 1, 18, 3, 5, 9, 8, 10], [1, 10, 9, 5, 6, 0, 15, 5, 9, 2, 16, 2, 1, 0, 16, 7, 6], [4, 13, 4, 2, 1, 1, 1, 3, 9, 4, 8, 3, 11, 1, 4, 1, 2], [18, 6, 2, 2, 5, 8, 2, 5, 0, 5, 6, 2, 2, 13, 9, 9, 3], [16, 3, 1, 0, 3, 0, 4, 2, 2, 2, 8, 4, 10, 5, 3, 10, 6], [2, 9, 17, 9, 1, 2, 3, 3, 22, 4, 9, 1, 6, 3, 1, 11, 7], [11, 3, 10, 9, 5, 8, 28, 7, 13, 13, 2, 13, 16, 15, 6, 6, 15], [5, 1, 7, 4, 11, 3, 6, 6, 10, 2, 1, 1, 4, 11, 5, 21, 11], [19, 3, 14, 5, 5, 8, 6, 18, 22, 5, 23, 15, 6, 11, 1, 19, 12], [0, 1, 2, 4, 7, 11, 3, 5, 7, 3, 12, 3, 1, 5, 3, 3, 7], [8, 7, 21, 3, 5, 11, 3, 2, 14, 7, 4, 6, 2, 1, 16, 4, 2], [10, 20, 4, 13, 6, 5, 22, 7, 4, 0, 19, 20, 1, 10, 11, 6, 13], [1, 5, 9, 1, 6, 1, 10, 4, 4, 5, 4, 3, 1, 2, 3, 8, 0], [6, 8, 15, 9, 4, 10, 14, 3, 0, 7, 2, 7, 9, 9, 6, 1, 7], [11, 20, 2, 7, 6, 10, 15, 4, 1, 1, 6, 11, 17, 3, 8, 7, 1], [1, 8, 0, 8, 10, 6, 5, 0, 5, 4, 4, 4, 0, 2, 10, 2, 5], [9, 10, 15, 15, 15, 5, 24, 6, 4, 11, 8, 6, 4, 18, 4, 10, 3]]
# logger.info(g)
class Printer:
    def __init__(self):
        self.eles = []

    def add_ele(self, ele):
        self.eles.append(ele)

    def print(self):
        if len(self.eles)==0:
            print(0)
        else:
            print(f"{len(self.eles)//2} {' '.join(map(str, self.eles))}")
        self.eles = []

class Day:
    def __init__(self):
        self.d = 0

    def acc(self):
        self.d += 1

class Task:
    def __init__(self, tasks):
        self.task_status = [False]*N
        self.tasks = tasks
        self.tasks_max_diff = []
        for task in tasks:
            task = sorted(task)
            self.tasks_max_diff.append(task[-1]-task[-2])
        self.cnts = [len(g_inv[u]) for u in range(N)]
        self.sims = [[cos_sim(self.tasks[i], self.tasks[j]) for j in range(N)] for i in range(N)]
        # TODO: 部分木サイズの計算
        self.n_child = [None]*N
        self.n_length = [None]*N
        cnts = [len(g[u]) for u in range(N)]
        q = [u for u in range(N) if cnts[u]==0]
        while q:
            u = q.pop()
            cnt = 1
            length = 0
            for v in g[u]:
                cnt += self.n_child[v]
                length = max(length, self.n_length[v])
            self.n_child[u] = cnt
            self.n_length[u] = length+1
            for v in g_inv[u]:
                cnts[v] -= 1
                if cnts[v] == 0:
                    q.append(v)
        self.n_child_max = max(self.n_child)
        self.n_length_max = max(self.n_length)
        self.available_task = set([u for u in range(N) if self.cnts[u]==0])
        self.task_norms = [math.sqrt(sum([i*i for i in self.tasks[task_id]])) for task_id in range(N)]

    def assign_task(self, task_id):
        self.task_status[task_id] = True
        self.available_task.remove(task_id)

    def task_finished(self, task_id):
        for v in g[task_id]:
            self.cnts[v] -= 1
            if self.cnts[v]==0:
                self.available_task.add(v)

    def score(self, task_id, member, mode=0):
        eps = 1e-7
        skill_norm_ = member.skill_norm
        task_norm_ = max(eps, self.task_norms[task_id])
        if R>=2000:
            n_edge     = [10, 10, 10, 10][mode] * len(g[task_id])
            n_child    = [10, 10, 10, 10][mode] * self.n_child[task_id]
            n_length   = [100, 100, 100, 100][mode] * self.n_length[task_id]
            max_diff   = [5, 5, 5, 0][mode] * self.tasks_max_diff[task_id]
            task_norm  = [0, 0, 0, 0][mode] * task_norm_
            n_new      = [10, 10, 10, 10][mode] * sum([self.cnts[v]==1 for v in g[task_id]])
            task_related_score = n_edge + n_child + n_length + max_diff + task_norm + n_new

            sim        = [0, 5, 10, 20][mode] * cos_sim(self.tasks[task_id], member.estimated_skill)
            my_sihyo   = [0, 0, 0, 0][mode] * skill_norm_/task_norm_
            pairwise_score = sim + my_sihyo
            return task_related_score*1000+pairwise_score
        else:
            n_edge     = [10, 10, 10, 10][mode] * len(g[task_id])
            n_child    = [10, 10, 10, 10][mode] * self.n_child[task_id]
            n_length   = [100, 100, 100, 100][mode] * self.n_length[task_id]
            max_diff   = [5, 5, 5, 0][mode] * self.tasks_max_diff[task_id]
            task_norm  = [-250, -250, 0, 0][mode] * task_norm_
            n_new      = [10, 10, 10, 10][mode] * sum([self.cnts[v]==1 for v in g[task_id]])
            task_related_score = n_edge + n_child + n_length + max_diff + task_norm + n_new

            sim        = [0, 50, 100, 200][mode] * cos_sim(self.tasks[task_id], member.estimated_skill)
            my_sihyo   = [100, 100, 100, 100][mode] * skill_norm_/task_norm_
            pairwise_score = sim + my_sihyo
            return task_related_score+pairwise_score

printer = Printer()
day = Day()
task = Task(tasks__)

class Member:
    def __init__(self, i):
        self.i = i
        self.ability = [1]*K
        self.cur_task = None
        self.cur_d = None
        self.past_task_id = []
        self.is_free = True
        self.printer = printer
        self.d = day
        self.task = task
        self.task_cnt = 0
        self.estimated_skill_lb = [0]*K
        self.estimated_skill = [0]*K
        self.cnt = [1]*K
        self.definite_skill = [None]*K
        self.skill_norm = math.sqrt(sum([i*i for i in self.estimated_skill]))

    def task_assign(self, task_id):
        self.cur_d = self.d.d
        self.cur_task_id = task_id
        self.printer.add_ele(self.i+1)
        self.printer.add_ele(task_id+1)
        self.task.assign_task(task_id)
        self.is_free = False

    def task_finished(self):
        self.task.task_finished(self.cur_task_id)
        self.past_task_id.append(self.cur_task_id)
        t = self.d.d-self.cur_d
        task = self.task.tasks[self.cur_task_id]
        self.task_cnt += 1
        self.cur_task_id = None
        self.cur_d = None
        self.is_free = True
        # TODO: スキル推定
        vec = [task[i]-t for i in range(K)]
        cnt = sum([v>=eslb for v, eslb in zip(vec, self.estimated_skill_lb)])
        w = K-cnt
        for i, (d, v, eslb, es) in enumerate(zip(task, vec, self.estimated_skill_lb, self.estimated_skill)):
            self.estimated_skill_lb[i] = max(eslb, d-(t+3))
            if v>=eslb:
                self.cnt[i] += w
                self.estimated_skill[i] = ((v+5)*w+es*(self.cnt[i]-w))/self.cnt[i]
        # self.estimated_skill = [s for s in S[self.i]]
        # self.estimated_skill_lb = [s for s in S[self.i]]
        # self.estimated_skill = self.estimated_skill_lb
        print_skill = [es for d, v, eslb, es in zip(task, vec, self.estimated_skill_lb, self.estimated_skill)]
        print(f"#s {self.i+1} {' '.join(map(str, print_skill))}")
        self.skill_norm = math.sqrt(sum([i*i for i in self.estimated_skill]))

members = [Member(i) for i in range(M)]
# init assign
q = []
for i in range(M):
    for task_id in task.available_task:
        s = task.score(task_id, members[i], mode=0)
        q.append((s, task_id, i))
for s, task_id, i in sorted(q)[::-1]:
    if (not task.task_status[task_id]) and members[i].is_free:
        members[i].task_assign(task_id)

printer.print()
rest = []
for d in range(1, 2001):
    n, *f = map(int, input().split())
    f = [i-1 for i in f]
    day.acc()
    if n==-1:
        for member in members:
            pass
            # logger.info([(ds, lb) for ds, lb in zip(member.definite_skill, member.estimated_skill_lb)])
        logger.info((R, day.d))
        sys.exit(0)
    elif n==0:
        printer.print()
        continue
    for i in f:
        members[i].task_finished()
    f = [i for i in range(M) if members[i].is_free]
    # TODO: task assign
    q = []
    cnt = 0
    for i in f:
        for task_id in task.available_task:
            mode = 1 + (day.d>=150) + (day.d>=300)
            s = task.score(task_id, members[i], mode=mode)
            q.append((s, task_id, i))
    for s, task_id, i in sorted(q)[::-1]:
        if (not task.task_status[task_id]) and members[i].is_free:
            n_new = sum([task.cnts[v]==1 for v in g[task_id]])
            members[i].task_assign(task_id)
            cnt += 1
            if cnt==len(f):
                break
    printer.print()
"""   # score matrix
    mode = 1 + (day.d>=150) + (day.d>=300)
    scores = sorted([(task.score(task_id, member, mode=mode), member.i, task_id) for member in members for task_id in task.available_task])[::-1]
    appeared_member = [False]*M
    appeared_task = [False]*N
    for score, i, task_id in scores:
        if appeared_member[i] or appeared_task[task_id]:
            continue
        appeared_member[i] = True
        appeared_task[task_id] = True
        if members[i].is_free:
            members[i].task_assign(task_id)
    printer.print()
"""
