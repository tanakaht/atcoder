import subprocess
import os
import optuna
import matplotlib.pyplot as plt

def func(param):
    a1, a2 = param
    res = subprocess.run(f"./cal_score.sh {a1} {a2}", shell=True, stdout=subprocess.PIPE).stdout.decode("utf-8").split('\n')[:-1]
    # scores = list(map(lambda x: int(x.split()[-1]), res[:-1]))
    score = int(res[-1])
    return score

def objective(trial): # 引数 (trial) はTrial型の値
    a1 = trial.suggest_loguniform("a1", 0.001, 100) # 試すxを指定範囲から選ぶ (parameter suggestion)
    a2 = trial.suggest_loguniform("a2", 0.001, 100) # 試すxを指定範囲から選ぶ (parameter suggestion)
    ret = func((a1, a2)) # 探索 (トライアル) の途中状態を持つ
    print(a1, a2, ret)
    return ret

study = optuna.create_study(direction="maximize") # 最適化処理を管理するstudyオブジェクト
study.optimize(objective, # 目的関数
               n_trials=300 # トライアル数
              )
print(study.best_value)
print(study.best_params)
plt.plot(range(len(study.trials)), [trial.value for trial in study.trials]); plt.show()
XYC = [(trial.params["a1"], trial.params["a2"], trial.value) for trial in study.trials]
plt.scatter([x for x, y, c in XYC], [y for x, y, c in XYC], c=[c for x, y, c in XYC], s=1); plt.colorbar(); plt.show()
plt.scatter([x for x, y, c in XYC], [y for x, y, c in XYC], c=[c for x, y, c in XYC], s=0.1); plt.colorbar(); plt.show()
plt.scatter([x for x, y, c in XYC], [y for x, y, c in XYC], c=[c for x, y, c in XYC], s=10); plt.colorbar(); plt.show()
plt.scatter([x for x, y, c in XYC], [y for x, y, c in XYC], c=[c for x, y, c in XYC], s=5); plt.colorbar(); plt.show()
plt.scatter([x for x, y, c in XYC], [y for x, y, c in XYC], c=[c for x, y, c in XYC], s=1); plt.colorbar(); plt.show()
