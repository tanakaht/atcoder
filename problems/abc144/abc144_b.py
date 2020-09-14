N = int(input())
for i in range(9, 0, -1):
    if N % i == 0:
        if N // i < 10:
            print('Yes')
        else:
            print('No')
        break
