def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    ret = abs(x1-x2)+abs(y1-y2)
    d = pow(3, 29)
    for i in range(29, -1, -1):
        d1 = (x1//d)%3
        d2 = (x2//d)%3
        if d1!=d2:
            break
        elif d1==d2==1 and abs(y1//d-y2//d)>=2:
            ret += min(2+(x1%d)+(x2%d), 2*d-((x1%d)+(x2%d)))
            ret -= abs((x1%d)-(x2%d))
            break
        d //= 3
    d = pow(3, 29)
    for i in range(29, -1, -1):
        d1 = (y1//d)%3
        d2 = (y2//d)%3
        if d1!=d2:
            break
        elif d1==d2==1 and abs(x1//d-x2//d)>=2:
            ret += min(2+(y1%d)+(y2%d), 2*d-((y1%d)+(y2%d)))
            ret -= abs((y1%d)-(y2%d))
            break
        d //= 3
    return ret


Q = int(input())
for i in range(Q):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    print(dist((a, b), (c, d)))
