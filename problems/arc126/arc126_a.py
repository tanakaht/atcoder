import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N2, N3, N4 = map(int, input().split())
    N6 = N3//2
    ans = 0
    ans += min(N4, N6)
    N4 -= ans
    N6 -= ans
    if N4:
        if N2 >= N4//2:
            ans += (4*N4+2*N2)//10
        else:
            ans += N2
    elif N6:
        if N2 >= N6*2:
            ans += (6*N6+2*N2)//10
        else:
            ans += N2//2
    else:
        ans += N2//5
    print(ans)
