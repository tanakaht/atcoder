import subprocess

result = {}
tmp = []
for a1 in [0, 1, 10, 100]:
    for a2 in [0, 1, 10, 100]:
        res = subprocess.run(f"./cal_score.sh {a1} {a2}", shell=True, stdout=subprocess.PIPE).stdout.decode("utf-8").split('\n')[:-1]
        scores = list(map(lambda x: int(x.split()[-1]), res[:-1]))
        score = int(res[-1])
        result[(a1, a2)] = (score, scores)
        tmp.append((score, a1, a2))
        print(a1, a2, score)
print(result)
print(sorted(tmp))
