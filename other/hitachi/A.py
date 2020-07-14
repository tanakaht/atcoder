S = input()
flg = True
while flg and len(S) >= 1:
    flg = (S[:2] == 'hi')
    S = S[2:]
print('Yes' if flg else 'No')
