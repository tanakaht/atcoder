N, Q = map(int, input().split())
s = [chr(i) for i in range(65, 65+N)]
n_query = 0


def quicksort(l):
    if len(l) <= 1:
        return l
    global n_query
    pivot = l[0]
    left, right = [], []
    for i in l[1:]:
        if n_query == Q:
            return l
        n_query += 1
        print(f'? {pivot} {i}')
        ans_query = input()
        if ans_query == '>':
            left.append(i)
        else:
            right.append(i)
    return quicksort(left) + [pivot] + quicksort(right)


print(f'! {"".join(quicksort(s))}', flush=True)
