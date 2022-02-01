# 素因数の個数分は絶対いる。それを構築できる
N = int(input())
kusi = [-1]*(N+1)
kusi[0] = 1
kusi[1] = 1
for i in range(2, N+1):
    if kusi[i]!=-1:
        continue
    for j in range(1, N//i+1):
        kusi[i*j] = i

def get_cnt(i):
    if i == 1:
        return 1
    return get_cnt(i//kusi[i])+1
A = [get_cnt(i) for i in range(1, N+1)]
print(' '.join(map(str, A)))
