import sys
import math
from logging import getLogger, StreamHandler, FileHandler, DEBUG
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
S = [list(map(int, input().split())) for _ in range(M)]
#for s in S:
#    print(s)
print(S)
