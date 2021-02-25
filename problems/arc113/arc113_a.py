K = int(input())
ans = 0
for i in range(1, K+1):
    for j in range(1, K//i+1):
        for k in range(1, K//(i*j)+1):
            ans += 1
print(ans)
