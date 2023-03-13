# Alexei Peter_I
# Anna Peter_I
# Elizabeth Peter_I
# Peter_II Alexei
# Peter_III Anna
# Paul_I Peter_III
# Alexander_I Paul_I
# Nicholaus_I Paul_I

N = int(input())
tree = dict()
tree['Peter_I'] = 0
for i in range(N):
    child, parent = input().split()
    tree[child] = tree[parent] + 1

print(tree, '\n')

for name in sorted(tree.keys()):
    print(name, tree[name])
