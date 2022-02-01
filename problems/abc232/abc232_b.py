S = map(lambda x: ord(x)-97, input())
T = map(lambda x: ord(x)-97, input())
x = set([(s-t)%26 for s, t in zip(S, T)])
print("Yes" if len(x)==1 else "No")
