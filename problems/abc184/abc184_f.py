N, T = map(int, input().split())
A = list(map(int, input().split()))
fhA = A[:N // 2]
shA = A[N // 2:]
fh_ptn = set([0])
for a in fhA:
    new_ptn = set()
    for ptn in fh_ptn:
        new_ptn.add(ptn)
        if ptn+a<=T:
            new_ptn.add(ptn + a)
    fh_ptn = new_ptn

sh_ptn = set([0])
for a in shA:
    new_ptn = set()
    for ptn in sh_ptn:
        new_ptn.add(ptn)
        if ptn+a<=T:
            new_ptn.add(ptn + a)
    sh_ptn = new_ptn

fh_ptn = sorted(fh_ptn)
sh_ptn = sorted(sh_ptn)[::-1]

j = 0
ans = 0
for i in range(len(fh_ptn)):
    while fh_ptn[i] + sh_ptn[j] > T:
        j += 1
    ans = max(ans, fh_ptn[i] + sh_ptn[j])
print(ans)
