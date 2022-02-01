import numpy as np

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    # エッジのリストから隣接リストへと変換
    g=[[] for _ in range(N)]
    for a, b in AB:
        g[a-1].append(b-1)
        g[b-1].append(a-1)

    # dfs２回
    x, _ = getFarthestNode(g, 0, N)
    y, length = getFarthestNode(g, x, N)
    print(length+1)

def getFarthestNode(g, start, N):
    dist = [-1] * N  # distance from start
    dist[start] = 0
    count = 0  # count of appeared node
    # 出現したノードを取っておくlist
    q = [start]
    count += 1
    # 出現したノードからたどれるノードをたどっていく
    # ノードを取り出す順番によってdfsとかbfsとか呼ばれる
    while True:
        # 出現済みノードを一つ取って
        u = q.pop()
        # それに隣接するものを探索する
        for v in g[u]:
            # 訪問済み(distが更新されている)ものは飛ばす
            if dist[v] != -1:
                continue
            # distを記録して出現済みノードに追加する
            count += 1
            dist[v] = dist[u]+1
            q.append(v)
        if count >= N:
            break
    node = np.argmax(dist)
    return node, dist[node]

if(__name__ == "__main__"):
    main()
