S = input()

def is_kaibun(s):
    # print(s[:len(s)//2], s[:(len(s)-1)//2:-1])
    return s[:len(s)//2] == s[:(len(s)-1)//2:-1]

flg = is_kaibun(S) and is_kaibun(S[:len(S)//2]) and is_kaibun(S[:len(S)//2:-1])

print('Yes' if flg else 'No')