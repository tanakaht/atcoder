a, b, n = map(int, input().split())
P =list(input().split())
results = []
tmpres = []
for p in P:
    if p == 'G':
        tmpres.append(0)
    else:
        tmpres.append(int(p))
    if sum(tmpres) == b:
        results.append(tmpres)
        tmpres = []
    elif len(tmpres) == 2 and len(results) < a-1:
        results.append(tmpres)
        tmpres = []
if tmpres:
    results.append(tmpres)

scores = [0]
last_pin = 0
last_2_pin = 0
for res in results[::-1]:
    if res[0] == b:
        scores.append(last_pin+last_2_pin+b)
        last_2_pin = last_pin
        last_pin = b
    elif sum(res) == b:
        scores.append(last_pin+b)
        last_2_pin = res[1]
        last_pin = res[0]
    else:
        scores.append(sum(res))
        if len(res) == 2:
            last_2_pin = res[1]
        else:
            last_2_pin = last_pin
        last_pin = res[0]
print(sum(scores))
