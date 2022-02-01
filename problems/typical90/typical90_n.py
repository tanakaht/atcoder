input()
print(sum([abs(i-j) for i,j in zip(sorted(list(map(int,input().split()))), sorted(list(map(int,input().split()))))]))
