N = int(input())
S = list(input())
Q = int(input())
TAB = [list(map(int, input().split())) for _ in range(Q)]
is_flip = False
for t, a, b in TAB:
    if t == 1:
        a -= 1
        b -= 1
        if is_flip:
            if a <N:
                a = a+N
            else:
                a = a-N
            if b <N:
                b = b+N
            else:
                b = b-N
            S[a], S[b] = S[b], S[a]
        else:
            S[a], S[b] = S[b], S[a]
    else:
        is_flip ^= 1

if is_flip:
    print(''.join(S[N:]+S[:N]))
else:
    print(''.join(S))
