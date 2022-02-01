import sys

chr2id = {"A": 0, "B": 1, "C": 2}
N = int(input())
S = [(chr2id[c]-i)%3 for i, c in enumerate(input())]
T = [(chr2id[c]-i)%3 for i, c in enumerate(input())]
S_, T_ = [], []
for s, t in zip(S, T):
    S_.append(s)
    T_.append(t)
    if len(S_)>=3 and S_[-1]==S_[-2]==S_[-3]:
        [S_.pop() for _ in range(3)]
    if len(T_)>=3 and T_[-1]==T_[-2]==T_[-3]:
        [T_.pop() for _ in range(3)]
if S_==T_:
    print("YES")
else:
    print("NO")
