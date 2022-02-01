N = int(input())
XY = sorted([list(map(int, input().split())) for _ in range(N)])
MOD = int(10**9+7)
dp0u = [[[0]*N for _ in range(N)] for _ in range(N)] # 始点, pre, now=>組み合わせ
dp0d = [[[0]*N for _ in range(N)] for _ in range(N)] # 始点, pre, now=>組み合わせ
dp1u = [[[0]*N for _ in range(N)] for _ in range(N)] # 始点, pre, now=>組み合わせ
dp1d = [[[0]*N for _ in range(N)] for _ in range(N)] # 始点, pre, now=>組み合わせ

def is_odd(i, j):
    xi, yi = XY[i]
    xj, yj = XY[j]
    return (abs(xi-xj)*abs(yi-yj))%2

def is_up(i, j, k):
    xi, yi = XY[i]
    xj, yj = XY[j]
    xk, yk = XY[k]
    if xi==xj:
        return yi<yj
    y = yi+(yj-yi)/(xj-xi)*(xk-xi)
    return yk>y

area = [[[0]*N for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i==j or j==k or k==i:
                continue
            xi, yi = XY[i]
            xj, yj = XY[j]
            xk, yk = XY[k]
            x1, y1 = xj-xi, yj-yi
            x2, y2 = xk-xi, yk-yi
            area[i][j][k] = abs(x1*y2-y1*x2)

def is_inside(i, j, k, l):
    return area[i][j][k] == (area[i][j][l]+area[i][k][l]+area[j][k][l])



# i, j, k内部の数
n_inside = [[[-3]*N for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            P = [XY[i], XY[j], XY[k], XY[i]]
            for l in range(N):
                n_inside[i][j][k] += is_inside(i, j, k, l)

pow2s = [pow(2, i, MOD) for i in range(N)]
for i in range(N):
    dp0u_ = dp0u[i]
    dp0d_ = dp0d[i]
    dp1u_ = dp1u[i]
    dp1d_ = dp1d[i]
    for j in range(i+1, N):
        if is_odd(i, j):
            dp1u_[i][j] = 1
            dp1d_[i][j] = 1
        else:
            dp0u_[i][j] = 1
            dp0d_[i][j] = 1
    for pre in range(i, N):
        for now in range(pre+1, N):
            dp0u_prenow = dp0u_[pre][now]
            dp0d_prenow = dp0d_[pre][now]
            dp1u_prenow = dp1u_[pre][now]
            dp1d_prenow = dp1d_[pre][now]
            dp0u_now = dp0u_[now]
            dp0d_now = dp0d_[now]
            dp1u_now = dp1u_[now]
            dp1d_now = dp1d_[now]
            for to_ in range(now+1, N):
                cnt = pow2s[n_inside[i][now][to_]]
                if is_up(pre, now, to_):
                    if is_odd(now, to_):
                        dp0d_now[to_] = (dp0d_now[to_]+dp1d_prenow*cnt)%MOD
                        dp1d_now[to_] = (dp1d_now[to_]+dp0d_prenow*cnt)%MOD
                    else:
                        dp0d_now[to_] = (dp0d_now[to_]+dp0d_prenow*cnt)%MOD
                        dp1d_now[to_] = (dp1d_now[to_]+dp1d_prenow*cnt)%MOD
                else:
                    if is_odd(now, to_):
                        dp0u_now[to_] = (dp0u_now[to_]+dp1u_prenow*cnt)%MOD
                        dp1u_now[to_] = (dp1u_now[to_]+dp0u_prenow*cnt)%MOD
                    else:
                        dp0u_now[to_] = (dp0u_now[to_]+dp0u_prenow*cnt)%MOD
                        dp1u_now[to_] = (dp1u_now[to_]+dp1u_prenow*cnt)%MOD
ans = 0
for i in range(N):
    for j in range(i+1, N):
        u0cnt, u1cnt, d0cnt, d1cnt = 0, 0, 0, 0
        for k in range(i, j):
            u0cnt = (u0cnt+dp0u[i][k][j])%MOD
            u1cnt = (u1cnt+dp1u[i][k][j])%MOD
            d0cnt = (d0cnt+dp0d[i][k][j])%MOD
            d1cnt = (d1cnt+dp1d[i][k][j])%MOD
        ans = (ans+u0cnt*d0cnt+u1cnt*d1cnt-1)%MOD
print(ans)
