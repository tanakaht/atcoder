import math
K = int(input())
divs = set()
for i in range(1, int(math.sqrt(K))+1):
    if K%i==0:
        divs.add(i)
        divs.add(K//i)
divs = sorted(divs)
ans = 0
for i in range(len(divs)):
    for j in range(i, len(divs)):
        ans += (K%(divs[i]*divs[j])==0) and (K//(divs[i]*divs[j])>=divs[j])
print(ans)
