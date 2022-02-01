from collections import deque

N = int(input())
S = input()
A = deque([])
for i, s in enumerate(S):
    if s == 'L':
        A.appendleft(i+1)
    elif s == 'R':
        A.append(i+1)

    elif s == 'A':
        if len(A)<=0:
            print('ERROR')
        else:
            tmp = [A.popleft() for _ in range(1)]
            print(tmp[-1])
            for j in tmp[-2::-1]:
                A.appendleft(j)
    elif s == 'B':
        if len(A)<=1:
            print('ERROR')
        else:
            tmp = [A.popleft() for _ in range(2)]
            print(tmp[-1])
            for j in tmp[-2::-1]:
                A.appendleft(j)
    elif s == 'C':
        if len(A)<=2:
            print('ERROR')
        else:
            tmp = [A.popleft() for _ in range(3)]
            print(tmp[-1])
            for j in tmp[-2::-1]:
                A.appendleft(j)

    elif s == 'D':
        if len(A)<=0:
            print('ERROR')
        else:
            tmp = [A.pop() for _ in range(1)]
            print(tmp[-1])
            for j in tmp[-2::-1]:
                A.append(j)
    elif s == 'E':
        if len(A)<=1:
            print('ERROR')
        else:
            tmp = [A.pop() for _ in range(2)]
            print(tmp[-1])
            for j in tmp[-2::-1]:
                A.append(j)
    elif s == 'F':
        if len(A)<=2:
            print('ERROR')
        else:
            tmp = [A.pop() for _ in range(3)]
            print(tmp[-1])
            for j in tmp[-2::-1]:
                A.append(j)
