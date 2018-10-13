dict = {'mile':1609.0000, 'yard':0.9144, 'foot':0.304800, 'inch':0.0254,'km':1000.0000, 'cm':0.0100, 'mm':0.0010, 'm':1.00}
a = input().split()
m = float(a[0]) * dict[a[1]]
out = m / dict[a[3]]
print('{:.2e}'.format(out))