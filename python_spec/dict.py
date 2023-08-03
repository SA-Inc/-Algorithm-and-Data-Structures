d1 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}

k1 = ('k1', 'k2', 'k3', 'k4', 'k5')

d2 = d1.copy()

d1.clear()

print('clear', d1)
print('copy', d2)

print('fromkeys', dict.fromkeys(k1, 0))

print('get', d2.get('c'))

print('items', d2.items())
print('keys', d2.keys())
print('values', d2.values())

d2.pop('c')

print('pop', d2)

d2.popitem()

print('popitem', d2)

d2.setdefault('f', 6)

print('setdefault', d2)

d2.update({'x': 24, 'y': 25, 'z': 26})

print('update', d2)
