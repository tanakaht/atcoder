N = int(input())
ans = [0]*(N+1)
f = lambda x, y, z: x**2 + y**2 + z**2 + x*y + y*z + z*x
root_N = int(N**0.5)

for x in range(1, root_N+1):
    for y in range(1, root_N+1):
        for z in range(1, root_N+1):
            i = f(x, y, z)
            if i <= N:
                ans[f(x, y, z)] += 1

print('\n'.join(map(str, ans[1:])))
