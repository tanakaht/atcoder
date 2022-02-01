from collections import defaultdict
c = defaultdict(int)
S = input()
mozi = set([chr(i) for i in range(97, 97+26)]+ ['(', ')'])
n = 0
bur_q = []
n_cum = 1
for s in S:
    if s not in mozi:
        n = n*10+int(s)
    elif s == '(':
        n = max(1, n)
        n_cum *= n
        bur_q.append(n)
        n = 0
    elif s == ')':
        n = max(1, n)
        deno = bur_q.pop()
        n_cum //= deno
        n = 0
    else:
        n = max(1, n)
        c[s] += n*n_cum
        n = 0
for s in [chr(i) for i in range(97, 97+26)]:
    print(s, c[s])
