import sys
import math
import random
from logging import LogRecord, getLogger, StreamHandler, FileHandler, DEBUG
from time import time
ts_start = time()
logger = getLogger(__name__)    #以降、このファイルでログが出たということがはっきりする。
handler = FileHandler("./log.txt")
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
EPS = 1e-7
def my_print(*s):
    print(*s)
    logger.info(f"stdout: {s}")

def my_input():
    ret = input()
    logger.info(f"stdin: {ret}")
    return ret


# 情報読み込み
my_print("budget")
C_init = int(input())

my_print("temporal")
T_max, T_last, N_div, N_day, N_acc = map(int, input().split()) # T_max=200, N_div=10なら10個の区間が存在し、その中で20個のステップをとる

my_print("score")
a_cost = int(input())
w_day = list(map(float, input().split()))
w_trans, w_ele, w_env, w_acc = map(float, input().split())
a_trans_fee, a_trans_penalty = map(float, input().split())
a_ele, a_ele_FE, a_ele_buy = map(float, input().split())
a_env_fuel, a_env_buy = map(float, input().split())
a_acc = int(input())


my_print("graph")
V, E = map(int, input().split())
vertexs = [list(map(int, input().split())) for _ in range(V)] # x, y,人口,面積,土地代
edges = [list(map(int, input().split())) for _ in range(E)] #u, v, d

my_print("demand")
N_demand = int(input())

demands = [[None]*(N_day) for _ in range(N_demand)]
for i in range(N_demand):
    for d in range(N_day):
        print("demand", d+1, i+1)
        x, sigma = map(int, input().split())
        D = list(map(int, input().split()))
        demands[i][d] = (x, sigma, D)

radiations = [[None]*(N_day) for _ in range(V)]
for i in range(V):
    for d in range(N_day):
        print("radiation", d+1, i+1)
        R = list(map(float, input().split()))
        radiations[i][d] = R

# my_print("radiation", day, id)

my_print("asset")
N_PV = int(input())
N_FE = int(input())
N_RB = int(input())
N_EVC = int(input())
N_V = int(input())

PVs = [None]*N_PV
for i in range(N_PV):
    print("asset", "PV", i+1)
    A_PV, C_PV_init = map(int, input().split())
    PVs[i] = (A_PV, C_PV_init)

FEs = [None]*N_FE
for i in range(N_FE):
    print("asset", "FE", i+1)
    P_FE_max, C_FE_init = map(int, input().split())
    FEs[i] = (P_FE_max, C_FE_init)

RBs = [None]*N_RB
for i in range(N_RB):
    print("asset", "RB", i+1)
    Cap_RB, C_RB_init = map(int, input().split())
    RBs[i] = (Cap_RB, C_RB_init)

EVCs = [None]*N_EVC
for i in range(N_EVC):
    print("asset", "EVC", i+1)
    P_EVC_in, P_EVC_out, C_EVC_init = map(int, input().split())
    EVCs[i] = (P_EVC_in, P_EVC_out, C_EVC_init)

Vehicles = [None]*N_V
for i in range(N_V):
    print("asset", "vehicle", i+1)
    Cap_V_ele, Cap_V_pop = map(int, input().split())
    P_V_charge, P_V_discharge, C_V_init, delta_V_move = map(int, input().split())
    Vehicles[i] = (Cap_V_ele, Cap_V_pop, P_V_charge, P_V_discharge, C_V_init, delta_V_move)

orders = [None]*N_day
for d in range(N_day):
    print("order", d+1)
    orders[d] = list(map(int, input().split()))

my_print("shelter")
N_shelter = int(input())
shelter_info = [list(map(int, input().split())) for _ in range(N_shelter)]
D_shelter = list(map(int, input().split()))

my_print("end")

class Grid:
    def __init__(self, demand):
        self.demand_prediction = [None]*N_day
        self.demand_prediction_sigma = [None]*N_day
        self.radiation_prediction = [None]*N_day
        for i in range(N_day):
            x, sigma, D = demand[i]
            self.idx = x-1
            self.demand_prediction[i] = D
            self.demand_prediction_sigma[i] = sigma
            self.radiation_prediction[i] = radiations[self.idx][i]
        self.x, self.y, self.p, self.A, self.l = vertexs[self.idx]  # x, y,人口,面積,土地代
        self.flg = False
        self.Chg_init = 0
        self.asset = {
            "PV": [0, 10],
            "FE": 0,
            "RB":[0, 10],
            "EVC": 1
        }
        self.evs = []

    def set_PV(self, v):
        """容量vを満たす最安の設置を行う, 見たせなければ、できるだけたくさん配置できるもの"""
        cost = math.inf
        for pv_type, (A_PV, C_init_PV) in enumerate(PVs):
            A = v*A_PV
            if A>self.A:
                continue
            tmp_cost = C_init_PV*v+A*self.l
            if cost > tmp_cost:
                cost = tmp_cost
                self.asset["PV"] = [pv_type, v]
        if cost!=math.inf:
            return
        pv_type, (A_PV, C_init_PV) = sorted(enumerate(PVs), key=lambda x: x[1][0])[0]
        v_ = self.A//A_PV
        self.asset["PV"] = [pv_type, v_]

    def set_RB(self, v):
        """容量vを満たす最安の設置を行う, 見たせなければ、できるだけたくさん配置できるもの"""
        cost = math.inf
        for rb_type, (Cap_RB, C_init_RB) in enumerate(RBs):
            tmp_cost = math.ceil(v/Cap_RB)*C_init_RB
            if cost > tmp_cost:
                cost = tmp_cost
                self.asset["RB"] = [rb_type, v]

    def adjust_EVC(self):
        """とりあえず、PV-demandのmax"""
        pass

grids = [Grid(demand) for demand in demands]


class Budget:
    def __init__(self, c_init):
        self.c_init = c_init

    def rest_budget(self):
        ret = self.c_init
        for grid in grids:
            ret -= PVs[grid.asset["PV"][0]][-1]*grid.asset["PV"][1]
            ret -= PVs[grid.asset["PV"][0]][0]*grid.asset["PV"][1]*grid.l
            ret -= FEs[grid.asset["FE"]][-1]
            ret -= RBs[grid.asset["RB"][0]][-1]*grid.asset["RB"][1]
            ret -= EVCs[grid.asset["EVC"]][-1]
            ret -= PVs[grid.asset["PV"][0]][1]*grid.asset["PV"][1]
            for ev_type, Chg_init in grid.evs:
                ret -= Vehicles[ev_type][-2]
        return ret

budget = Budget(C_init)

def print_infos():
    my_print(sum([grid.flg for grid in grids]))
    for grid in grids:
        if not grid.flg:
            continue
        my_print(grid.idx+1, grid.Chg_init)
        my_print(grid.asset["PV"][0]+1, grid.asset["PV"][1])
        my_print(grid.asset["FE"]+1)
        my_print(grid.asset["RB"][0]+1, grid.asset["RB"][1])
        my_print(grid.asset["EVC"]+1)
    my_print(sum([len(grid.evs) for grid in grids]))
    for grid in grids:
        for ev in grid.evs:
            my_print(grid.idx+1, ev[1], ev[0]+1)

def test(d, opt):
    ts = time()
    print_infos()
    my_print("test", d+1, opt)
    S_trans, S_ele, S_env = map(float, my_input().split())
    logger.info(f"test in {time()-ts} second, S_trans={S_trans}, S_ele={S_ele}, S_env={S_env}")
    return S_trans, S_ele, S_env

def submit(opt):
    print_infos()
    my_print("submit", 1, opt)


# とりあえず、1台ずつ　EV買う
for grid in grids:
    for _ in range(1):
        v_id = 0
        Cap_V_ele, Cap_V_pop, P_V_charge, P_V_discharge, C_V_init, delta_V_move = Vehicles[v_id]
        grid.evs.append((v_id, Cap_V_ele))

for grid in grids:
    grid.flg = True
for grid in grids:
    A_PV, C_PV_init = PVs[grid.asset["PV"][0]]
    rest_budget = budget.rest_budget()
    rps = [sum(rp) for rp in grid.radiation_prediction]
    rates = [sum(dp)/sum(rp) for dp, rp in zip(grid.demand_prediction, grid.radiation_prediction)]
    v_PV = sorted(rates)[len(rates)//2]*2
    grid.set_PV(math.ceil(v_PV))
    v_RB = sorted(rps)[len(rps)//2]/10
    grid.set_RB(math.ceil(v_RB))


logger.info(str(Vehicles))
logger.info(str(C_init))

# logger.info(test(0, N_demand//2))
submit(N_demand//2) # テキトーに1/2
