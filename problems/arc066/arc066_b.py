N = int(input())
P = int(1e9+7)
def solve_naive(N):
    ans = 0
    for i in range(N+1):
        ans = (ans+bin(i).count("1"))%P
    for i in range((N+1)//2, N+1):
        for j in range(N):
            ans -= ((i|j)-i!=0)
        ans = (ans+bin(i).count("1"))%P
    return i
