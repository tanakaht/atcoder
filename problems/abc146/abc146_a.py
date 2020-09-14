days = 'SUN, MON, TUE, WED, THU, FRI, SAT'.split(', ')
S = input()
ans = (7 - days.index(S))
print(ans)
