N = int(input())
print('? '+' '.join(map(str, range(1, N+1))))
base = input()

def is_ok(arg):
    print('? '+' '.join(map(str, range(arg, N+arg))))
    s = input()
    return s == base

def bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
i = bisect(N+1, 1)+1

ans = ['']*(2*N+1)
if base == 'Red':
    ans[i-1] = 'R'
    ans[i+N-1] = 'B'
else:
    ans[i-1] = 'B'
    ans[i+N-1] = 'R'
base_set = set(range(i, i+N-1))
query_s = '? '+' '.join(map(str, base_set)) if base_set else '?'
R_cnt, B_cnt = 0, 0
base_set2 = set()
for i in range(1, 2*N+1):
    if i in base_set or ans[i] != '':
        continue
    print(f'{query_s} {i}')
    s = input()
    if s=='Red':
        ans[i] = 'R'
        if R_cnt < N//2:
            base_set2.add(i)
            R_cnt+=1
    else:
        ans[i] = 'B'
        if B_cnt < N//2:
            base_set2.add(i)
            B_cnt+=1
query_s = '? '+' '.join(map(str, base_set2)) if base_set2 else '?'
for i in base_set:
    print(f'{query_s} {i}')
    s = input()
    ans[i] = 'R' if s == 'Red' else 'B'
print('! ' + ''.join(map(str, ans[1:])))
