A = int(input())
B = int(input())
anss = set([1, 2, 3])
anss.remove(A)
anss.remove(B)
for i in anss:
    print(i)
