X = int(input())
if X>=90:
    print("expert")
else:
    for x in [40, 70, 90]:
        if x>X:
            print(x-X)
            break
