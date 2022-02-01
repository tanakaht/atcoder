N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(range(N))-A-set([0])
kitei = set()
C = []
for b in B:
    flg = True
    b_ = b
    for c in C:
        if 1<<(c.bit_length()-1) & b_:
            b_ ^= c
    if b_ != 0:
        kitei.add(b)
        C.append(b_)
        C = sorted(C)[::-1]

q = [0]
UV = []
appeared = [False]*N
appeared[0]=True
while q:
    u = q.pop()
    for b in kitei:
        if not appeared[u^b]:
            UV.append((u, u^b))
            appeared[u^b] = True
            q.append(u^b)
if len(UV)!=N-1:
    print(-1)
else:
    for u, v in UV:
        print(u, v)
