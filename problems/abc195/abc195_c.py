N = int(input())
n = len(str(N))-1
def count_comma(i):
    return i//3
ans = 0
for i in range(n):
    ans += count_comma(i) * 9 * pow(10, i)
ans += (N-pow(10, n)+1)*count_comma(n)
print(ans)
