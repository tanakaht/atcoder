N = int(input())
A = list(map(int, input().split()))
bits = set()
def find_next(S1, S2, from_bit):
    for i in range(from_bit, 31):
        appered = set()
        found = False
        for s in S1:
            appered.add(s//(1<<(30-i)))
        for s in S2:
            if s in appered:
                found = True
                break






for i in range(31):
