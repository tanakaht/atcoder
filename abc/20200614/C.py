X, N = map(int, input().split())
p = set(map(int, input().split()))
def main():
    if X not in p:
        print(X)
        return
    for i in range((N-1)//2+2):
        if X-i not in p:
            print(X-i)
            break
        elif X+i not in p:
            print(X+i)
            break

main()