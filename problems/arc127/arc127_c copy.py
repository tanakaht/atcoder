import sys

N = int(input())
X = list(input())
X = ['0']*(N-len(X))+X
for n in range(1, 33):
    kurisage = False
    na = list(bin(n)[2:])
    na = ['0']*(N-len(na))+na
    Xmn = []
    for i in range(N-1, -1, -1):
        if int(X[i])<int(na[i])+kurisage:
            Xmn.append("1")
            kurisage = True
        elif int(X[i])==int(na[i])+kurisage:
            Xmn.append("0")
            kurisage = False
        elif int(X[i])>int(na[i])+kurisage:
            Xmn.append("1")
            kurisage = False
    Xmn.append("1")
    Xmn = Xmn[::-1]
    cnt = 1
    flg = False
    ans = []
    for s in Xmn:
        if cnt>n:
            if s=="1":
                flg = True
                break
        elif cnt == n:
            if s=="1":
                ans.append(s)
            else:
                cnt += 1
        else:
            cnt += s=="0"
            ans.append(s)
    if flg or cnt<n:
        continue
    print(''.join(ans))
    sys.exit(0)

print(1)





def tmP():
    st.init([x=='1' for x in X])
    next1 = [None]*N
    pres = []
    for i, x in enumerate(X):
        if x=='1':
            for pre in pres:
                next1[pre] = i
            pre = [i]
        else:
            pres.append(i)

    x = 23
    x.bit_length()
    # X[i:]がnより大きいか
    def is_larger(i, n):
        if n< 0:
            return True
        if st.query(i, n.bit_length()-1):
            return True
        else:
            return X[-n.bit_length():] >= X

    for n in range(N):

        x = X[i]
        if is_larger(i+1, n):
            ans.append(x)
        else:
            break
        if x=='1':
            if is_larger(i+1, n):
                ans.append("1")
                n += 1
            elif is_larger(i, n):
                ans.append("0")
                n += 1
                n -= 1<<i
            else:
                break
        else:
            if is_larger(i+1, n+1):
                ans.append("0")
            else:
                break
    print("".join(ans))
