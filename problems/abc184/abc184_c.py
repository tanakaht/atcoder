import sys

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

def can_move(a, b, c, d):
    return ((a + b) == (c + d)) or ((a - b) == (c - d)) or (abs(a - c) + abs(b - d) <= 3)

if r1 == r2 and c1 == c2:
    print(0)
    sys.exit()
elif can_move(r1, c1, r2, c2):
    print(1)
    sys.exit()
else:
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        sys.exit()
    for x in range(r1 - 2, r1 + 3):
        for y in range(c1 - 2, c1 + 3):
            if can_move(x, y, r2, c2):
                print(2)
                sys.exit()
    for d in [(3, 0), (0, 3), (-3, 0), (0, -3)]:
        x, y = r1+d[0], c1+d[1]
        if can_move(x, y, r2, c2):
            print(2)
            sys.exit()
    print(3)
