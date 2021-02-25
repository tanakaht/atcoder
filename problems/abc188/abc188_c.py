N = int(input())
A = list(map(int, input().split()))
pre_i, pre_v = 0, A[0]
lat_i, lat_v = pow(2,N-1), A[pow(2, N-1)]
for i in range(pow(2,N-1)):
    if pre_v < A[i]:
        pre_i, pre_v = i, A[i]
for i in range(pow(2,N-1), pow(2,N)):
    if lat_v < A[i]:
        lat_i, lat_v = i, A[i]

ans = pre_i if pre_v < lat_v else lat_i

print(ans+1)
