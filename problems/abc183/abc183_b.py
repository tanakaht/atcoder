Sx, Sy, Gx, Gy = map(int, input().split())

ans = Sx + (Gx-Sx) * Sy / (Sy + Gy)
print(ans)
