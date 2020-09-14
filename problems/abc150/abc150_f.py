import re

N = int(input())
A = list(map(lambda x: bin(int(x))[2:], input().split()))
B = list(map(lambda x: bin(int(x))[2:], input().split()))
keta = max(max(map(len, A)), max(map(len, B)))


def xor(a, b):
    while keta > len(b):
        b = '0' + b
    while keta > len(a):
        a = '0' + a
    ret = ''
    for a_, b_ in zip(a, b):
        ret += '0' if a_ == b_ else '1'
    return ret


def create_table(pattern):
    table = [0 for _ in range(len(pattern)+1)]
    j = 0
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
        else:
            table[i] = j
            j = 0
    table[i+1] = j
    return table


def kmp_search(string, pattern):
    ret = []
    table = create_table(pattern)
    i = j = 0
    while i < len(string):
        if string[i] == pattern[j]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = table[j]
        if j == len(pattern):
            ret.append(i - j)
            j = table[j]
    else:
        return ret

def bm_search(string, pattern):
    ret = []
    pat_len = len(pattern)
    skip = [pat_len for _ in range(256)]
    for i in range(pat_len):
        skip[ord(pattern[i])] = pat_len - i - 1
    i = pat_len - 1
    while i < len(string):
        j = pat_len - 1
        while string[i] == pattern[j]:
            if j == 0:
                ret.append(i)
            i -= 1
            j -= 1
        i = i + max(skip[ord(string[i])], pat_len-j)
    return ret


C, D = [], []
for i in range(N-1):
    C.append(xor(A[i], A[i+1]))
    D.append(xor(B[i], B[i + 1]))
C.append(xor(A[-1], A[0]))
D.append(xor(B[-1], B[0]))
for k in kmp_search(D + D, C)[::-1]:
    if k == 0:
        continue
    print(N-k, int(xor(A[N-k], B[0]), 2))
