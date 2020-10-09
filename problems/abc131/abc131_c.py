from math import gcd
A, B, C, D = map(int, input().split())
cd = C*D//gcd(C, D)
ans = (B - A + 1)
ans -= (B // C - (A - 1) // C)
ans -= (B // D - (A - 1) // D)
ans += (B // cd - (A-1) // cd)
print(ans)
