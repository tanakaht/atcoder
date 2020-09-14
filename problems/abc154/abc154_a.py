S, T = input().split()
A, B = map(int, input().split())
U = input()
A -= S == U
B -= T==U
print(f'{A} {B}')
