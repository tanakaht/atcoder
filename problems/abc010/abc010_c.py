"""
感想
- forぶん回すだけのクソ簡単な問題
- せっかくなので遊んだ
  - distの計算しかしないけど一回書いたきりで使ってなかったVecを使う
  - YNEOS
"""
import sys, math

input = sys.stdin.readline

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        return Vec(self.x+x, self.y+y)

    def rotate(self, theta):
        x = self.x * math.cos(theta) - self.y * math.sin(theta)
        y = self.x * math.sin(theta) + self.y * math.cos(theta)
        return Vec(x, y)

    def theta(self):
        if self.x == 0:
            if self.y > 0:
                return math.pi/2
            elif self.y < 0:
                return 3* math.pi / 2
            else:
                return 0
        ret = math.atan(self.y / self.x)
        if self.x < 0:
            ret += math.pi
        return ret

    def dist(self, other):
        return math.sqrt((self.x - other.x)** 2 + (self.y - other.y)** 2)

    def __str__(self):
        return f'{self.x}, {self.y}'


txa, tya, txb, tyb, T, V = map(int, input().split())
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

from_ = Vec(txa, tya)
to_ = Vec(txb, tyb)

flg = False
for x, y in XY:
    p = Vec(x, y)
    flg = flg or (from_.dist(p) + p.dist(to_))/V <= T  # 0含むんか？
print('YNEOS'[not flg::2])
