from duration import Duration

d1 = Duration(4, 3)
d2 = Duration(1, -2)

print(f'd1 = {d1}')
print(f'd2 = {d2}')

d3 = d1 + d2
d4 = d1 - d2

print(f'd3 = {d3}')
print(f'd4 = {d4}')
