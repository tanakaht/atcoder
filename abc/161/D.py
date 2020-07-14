K = int(input())
# 10桁までやれば十分
runrun_table = [[0 for _ in range(10)] for _ in range(10)]
# i桁のルンルン数の種類 <= 3**(i-1)*9
for i in range(10):
    runrun_table[0][i] = 1
for keta in range(1, 10):
    for i in range(10):
        if i == 0:
            runrun_table[keta][i] = runrun_table[keta - 1][i] + \
                                    runrun_table[keta - 1][i + 1]
        elif i == 9:
            runrun_table[keta][i] = runrun_table[keta - 1][i - 1] + \
                                    runrun_table[keta - 1][i]
        else:
            runrun_table[keta][i] = runrun_table[keta - 1][i - 1] + \
                                    runrun_table[keta - 1][i] + \
                                    runrun_table[keta - 1][i + 1]

keta = 0
ans = ''
while sum(runrun_table[keta][1:]) < K:
    K -= sum(runrun_table[keta][1:])
    keta += 1

for piv in range(1, 10):
    if runrun_table[keta][piv] >= K:
        ans += str(piv)
        keta -= 1
        break
    K -= runrun_table[keta][piv]

while keta >= 0:
    if piv == 0:
        piv_range = [0, 1]
    elif piv == 9:
        piv_range = [8, 9]
    else:
        piv_range = range(piv-1, piv+2)
    for piv in piv_range:
        if runrun_table[keta][piv] >= K:
            ans += str(piv)
            keta -= 1
            break
        K -= runrun_table[keta][piv]

print(ans)
