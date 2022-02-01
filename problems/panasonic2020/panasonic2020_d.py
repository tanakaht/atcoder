import itertools
N = int(input())
ans = set()
alphas = 'abcdefghijklmnopq'
for idxs in itertools.product(*[list(range(i+1)) for i in range(N)]):
    s = ['a']
    for i in range(1, N):
        if idxs[i]==i:
            for x in alphas:
                if x not in s:
                    s.append(x)
                    break
        else:
            s.append(s[idxs[i]])
    ans.add(''.join(s))
print('\n'.join(sorted(ans)))
