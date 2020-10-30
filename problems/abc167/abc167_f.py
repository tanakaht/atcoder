import sys

N = int(input())
brackets_pos = []
brackets_neg = []
left_sum = 0
for _ in range(N):
    S = input()
    left_needs = 0
    left_cnt = 0
    for s in S:
        if s == '(':
            left_cnt += 1
        else:
            left_cnt -= 1
            left_needs = max(left_needs, -1 * left_cnt)
    if left_cnt >= 0:
        brackets_pos.append((left_needs, left_cnt))
    else:
        brackets_neg.append((left_needs, left_cnt))
    left_sum += left_cnt

if left_sum != 0:
    print('No')
    sys.exit(0)

brackets_pos = sorted(brackets_pos, key=lambda x: x[0])[::-1]
brackets_neg = sorted(brackets_neg, key=lambda x: x[0]+x[1])
cur_left_cnt = 0
while len(brackets_pos) > 0:
    left_needs, left_cnt = brackets_pos.pop()
    if left_needs > cur_left_cnt:
        print('No')
        sys.exit()
    cur_left_cnt += left_cnt
while len(brackets_neg) > 0:
    left_needs, left_cnt = brackets_neg.pop()
    if left_needs > cur_left_cnt:
        print('No')
        sys.exit()
    cur_left_cnt += left_cnt
print('Yes')
