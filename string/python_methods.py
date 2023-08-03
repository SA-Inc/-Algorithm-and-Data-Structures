str1 = 'some text'
str2 = 'Some text'
str3 = 'SomeText'
str4 = 'START\tSome\tText\tEND'
str5 = '{s} {n} {b} {no}'
str6 = '{x} {y}'
str7 = 'START\nSome\nText\nEND'
str8 = '   Some      '

print('capitalize', str1.capitalize())
print('casefold', str2.casefold())
print('center', str3.center(20, '*'))
print('count', str1.count('om', 0, 8))
print('encode', str1.encode())
print('endswith', str1.endswith('t'))
print('expandtabs', str4.expandtabs(2))

print('index', str1.index('m'))
print('find', str1.find('t'))

print('format', str5.format(s = 'iddqd', n = 34, b = True, no = None))
print('format_map', str6.format_map({'x': 3, 'y': 4}))


print('isalnum', str1.isalnum())
print('isalpha', str1.isalpha())
print('isascii', str1.isascii())
print('isdecimal', str1.isdecimal())
print('isdigit', str1.isdigit())
print('isidentifier', str1.isidentifier())
print('islower', str1.islower())
print('isnumeric', str1.isnumeric())
print('isprintable', str1.isprintable())
print('isspace', str1.isspace())
print('istitle', str1.istitle())
print('isupper', str1.isupper())

print('join', '#'.join(['12', '14', '16']))
print('join', '#'.join(('12', '14', '16')))
print('join', '#'.join({'a': '12', 'b': '14', 'c': '16'}))

print('ljust', str1.ljust(20, '-'), 'after')
print('rjust', str1.rjust(20, '-'), 'before')

print('lower', str3.lower())
print('upper', str1.upper())

print('upper', str1.maketrans('so', 'pe', 't'))
print('upper', str1.translate(str1.maketrans('so', 'pe', 't')))

print('partition', str1.partition('me'))
print('rpartition', str1.rpartition('me'))

print('replace', str1.replace('so', 'co', 2))

print('rindex', str1.rindex('t'))
print('rfind', str1.rfind('t'))

print('rsplit', str4.rsplit('\t'))
print('split', str4.split('\t'))

print('strip', str8.strip(' '))
print('rstrip', str8.rstrip(' '))
print('lstrip', str8.lstrip(' '))

print('splitlines', str7.splitlines())

print('startswith', str7.startswith('START'))

print('swapcase', str3.swapcase())
print('title', str1.title())

print('zfill', '56'.zfill(4))

