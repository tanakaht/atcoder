N, M = map(int, input().split())
N, M = max(N, M), min(N, M)
if M==1:
    if N==1:
        print(1)
    else:
        print(N-2)
else:
    print((N-2)*(M-2))
