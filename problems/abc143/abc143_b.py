N = int(input())
d = list(map(int, input().split()))
sumd = sum(d)
d_2 = sum([i * i for i in d])
print((sumd*sumd-d_2)//2)
