N, K = input().split()
K = int(K)
# N = int(N, base=8)
def eight2nine(s):
    x = 0
    tmp = 1
    for i, v in enumerate(s[::-1]):
        x += tmp*int(v)
        tmp *= 8
    ret = []
    while x:
        ret.append(str(x%9))
        x //= 9
    if not ret:
        ret = ["0"]
    return ''.join(ret[::-1])
for _ in range(K):
    N = eight2nine(N).replace('8', '5')
print(N)
