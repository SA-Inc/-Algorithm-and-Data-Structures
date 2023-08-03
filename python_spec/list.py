l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

l1.append(10)

print('append', l1)

l2 = l1.copy()

l1.clear()

print('clear', l1)
print('copy', l2)

print('count', l2.count(6))

l2.extend([11, 12, 13, 14, 15])

print('extend', l2)

print('index', l2.index(6))

l2.insert(5, 999)

print('insert', l2)

l2.pop()

print('pop', l2)

l2.remove(999)

print('remove', l2)

l2.reverse()

print('reverse', l2)

l3 = [12, 45, 1, 76, 32, 87, 63, 23, 34]

l3.sort()

print('sort', l3)



t1 = (1, 2, 3, 4, 5)

print('reverse', t1.count(3))
print('reverse', t1.index(3))
