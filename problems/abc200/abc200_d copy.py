import sys
N = int(input())
A = list(map(int, input().split()))
pre = [None]*200
ans = None
for i, a in enumerate(A):
    i += 1
    new = [None]*200
    if pre[a%200] is not None:
        ans = (pre[a%200], [i])
        print('Yes')
        print(len(ans[0]), *ans[0])
        print(len(ans[1]), *ans[1])
        sys.exit(0)
    elif pre[0] is not None:
        ans = (pre[0]+[i], [i])
        print('Yes')
        print(len(ans[0]), *ans[0])
        print(len(ans[1]), *ans[1])
        sys.exit(0)
    else:
        new[a%200] = [i]
    for rest, vs in enumerate(pre):
        if vs is None:
            continue
        if pre[(rest+a)%200] is not None:
            ans = (pre[(rest+a)%200], vs+[i])
            print('Yes')
            print(len(ans[0]), *ans[0])
            print(len(ans[1]), *ans[1])
            sys.exit(0)
        new[rest] = vs
        new[(rest+a)%200] = vs+[i]

    pre = new
print('No')
