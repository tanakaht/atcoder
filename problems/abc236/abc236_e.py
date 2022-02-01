import sys
N = int(input())
A = list(map(int, input().split()))


def is_ok(arg):
    flg = True
    ret = []
    for a in A:
        if a>=arg:
            flg = True
            ret.append(a)
        else:
            if not flg:
                ret.append(a)
            flg = False
    return ret[len(let)//2]




def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


ans1 = 0
ans2 = bisect(max(A)+1, min(A))
print(ans1, ans2)
