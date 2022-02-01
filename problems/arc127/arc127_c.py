import sys

N = int(input())
X = list(input())
X = ['0']*(N-len(X))+X
def X_minus1(i):
    for j in range(N-1, i-1, -1):
        if X[j]=="1":
            X[j] = "0"
            return True
        else:
            X[j] = "1"
    return False
X_minus1(0)
ans = ["1"]
for i in range(N):
    if X[i]=="1":
        ans.append("1")
    else:
        flg = X_minus1(i)
        if flg:
            ans.append("0")
        else:
            break
print("".join(ans))
