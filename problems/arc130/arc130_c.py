a = {i: 0 for i in range(10)}
b = {i: 0 for i in range(10)}
for i in input():
    a[int(i)] += 1
for i in input():
    b[int(i)] += 1

flip_flg = sum(a.values()) < sum(b.values())
if flip_flg:
    a, b = b, a

tmpa, tmpb = [], []
for i in range(10):
    tmpa += [i]*a[i]
    tmpb += [i]*b[i]
anscnt, ans = 0, (tmpa, tmpb)
for ten_a in range(10):
    a_ = {k: v for k, v in a.items()}
    b_ = {k: v for k, v in b.items()}
    if a_[ten_a] == 0:
        continue
    for ten_b in range(10-ten_a, 10):
        if b_[ten_b] != 0:
            break
    if b_[ten_b] == 0:
        continue
    a_[ten_a] -= 1
    b_[ten_b] -= 1
    ans_a, ans_b = [ten_a], [ten_b]
    rest_a, rest_b = [], []
    anscnt_ = 1
    for ai in range(1, 10):
        for bi in range(9-ai, 10):
            cnt = min(a_[ai], b_[bi])
            ans_a += [ai]*cnt
            ans_b += [bi]*cnt
            a_[ai] -= cnt
            b_[bi] -= cnt
            anscnt_ += cnt
        if sum(b_.values())==0:
            break
        rest_a += [ai]*a_[ai]
        a_[ai] = 0
    if sum(b_.values())==0:
        cnt = a_[9]
        ans_a += [9]*cnt
        anscnt_ += cnt
        a_[9] -= cnt
    for ai in range(10):
        rest_a += [ai]*a_[ai]
    for bi in range(10):
        rest_b += [bi]*b_[bi]
    if anscnt_ > anscnt:
        ans = ((ans_a+rest_a)[::-1], (ans_b+rest_b)[::-1])
        anscnt = anscnt_

if flip_flg:
    ans = (ans[1], ans[0])
print("".join(map(str, ans[0])))
print("".join(map(str, ans[1])))
