import sys

S = input()
T = input()
if S==T:
    print('Yes')
    sys.exit()

for i in range(len(S)-1):
    S_ = S[:i]+S[i+1]+S[i]+S[i+2:]
    if S_==T:
        print('Yes')
        sys.exit()
print('No')
