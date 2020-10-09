K = int(input())

def S(i):
    return sum(map(int, str(i)))

pre_ans = 0
diff = 1
for i in range(K):
    ans = pre_ans + diff
    while ans / S(ans) > diff:
        diff *= 10
        ans += (diff - 1) - (ans % diff)
    print(ans)
    pre_ans = ans
