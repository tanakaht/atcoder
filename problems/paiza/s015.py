k, s, t = map(int, input().split())

def get(k, s):
    if k == 1:
        return 'ABC'[s]
    lenk_1 = pow(2, k-1)*3-3
    # a abc b abc c
    if s == 0:
        return 'A'
    elif 0 < s < lenk_1+1:
        return get(k-1, s-1)
    elif s == lenk_1+1:
        return 'B'
    elif s < 2*lenk_1+2:
        return get(k-1, s-lenk_1-2)
    else:
        return 'C'

ans = [get(k, i-1) for i in range(s, t+1)]
print(''.join(ans))
