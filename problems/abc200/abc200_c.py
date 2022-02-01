N = int(input())
A = list(map(int, input().split()))
rests = [0]*200
for a in A:
    rests[a%200] += 1
ans = 0
for cnt in rests:
    ans += max(0, cnt*(cnt-1)//2)
print(ans)
