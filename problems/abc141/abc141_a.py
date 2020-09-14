S = input()
l = ['Sunny', 'Cloudy', 'Rainy']
d = {k: v for k, v in zip(l, l[1:])}
d[l[-1]] = l[0]
print(d[S])
