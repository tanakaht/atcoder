import sys
S = input()
T = "oxx"
for i in range(3):
    flg = True
    for j in range(len(S)):
        flg = flg & (S[j]==T[(i+j)%3])
    if flg:
        print("Yes")
        sys.exit(0)
print("No")
