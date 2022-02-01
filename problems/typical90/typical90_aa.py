N = int(input())
appeared = set()
for i in range(N):
    s = input()
    if s not in appeared:
        appeared.add(s)
        print(i+1)
