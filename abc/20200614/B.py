X, Y = map(int, input().split())
i = Y-2*X
flag = i%2==0 and i//2 <= X and i>=0
ans = 'Yes' if flag else 'No'
print(ans)
