N = int(input())
A = list(map(int, input().split()))
deno = sum(map(lambda x: 1 / x, A))
print(1/deno)
