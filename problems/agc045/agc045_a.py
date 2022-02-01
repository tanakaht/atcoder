T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))[::-1]
    S = input()[::-1]
    bases = []
    flg = True
    for s, a in zip(S, A):
        if s=='0':
            for i in range(len(bases)):
                if bases[i]<a:
                    bases[i], a = a, bases[i]
                if bases[i].bit_length()==a.bit_length():
                    a ^= bases[i]
            if a!=0:
                bases.append(a)
        elif s=='1':
            for i in range(len(bases)):
                if bases[i].bit_length()==a.bit_length():
                    a ^= bases[i]
            if a!=0:
                flg = False
                break
    if flg:
        print(0)
    else:
        print(1)
