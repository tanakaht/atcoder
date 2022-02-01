N = int(input())
S = input()
X = input()
ao_turns = [i=='A' for i in X[::-1]]
tmp = 1
rests = []
for i in S[::-1]:
    rests.append((int(i)*tmp)%7)
    tmp = (tmp*10)%7

taka_win = [1, 0, 0, 0, 0, 0, 0] # takaがかつrest=>True
for ao_turn, rest in zip(ao_turns, rests):
    if ao_turn:
        taka_win = [taka_win[i] and taka_win[(i+rest)%7] for i in range(7)]
    else:
        taka_win = [taka_win[i] or taka_win[(i+rest)%7] for i in range(7)]
if taka_win[0]:
    print('Takahashi')
else:
    print('Aoki')
