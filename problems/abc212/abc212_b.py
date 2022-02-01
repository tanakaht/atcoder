import sys
X = list(map(int, input()))
if len(set(X))==1:
    print('Weak')
    sys.exit(0)
for i in range(3):
    if (X[i]+1)%10!=X[i+1]:
        print('Strong')
        sys.exit(0)
print('Weak')
