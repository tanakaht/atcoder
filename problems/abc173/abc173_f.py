N = int(input())
UV = [tuple(map(int, input().split())) for _ in range(N-1)]
v_count = 0
e_count = 0
for n in range(1, N + 1):
    v_count += n * (N-n+1)
for u, v in UV:
    e_count += min(u, v)*(N-max(u, v)+1)
print(v_count-e_count)