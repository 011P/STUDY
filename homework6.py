#1(2)
my_dict = {'a': 123456, 'b': 234156, 'c': 342156}
print('2.1:     Dict:                    ',my_dict)
print('2.2.1:   Existing value:          ',my_dict['a'])
print('2.2.2:   Not existing value:      ',my_dict.get('d'))

my_dict.update({'d': 444433,
                'e': 555544})

delted = my_dict.pop('d')
print('2.3:     Deleted value:           ',delted)
print('2.4:     Modified dictionary:     ',my_dict)

#2(3)
my_set = {'1': 9, '1': 10, '2': 7, '2': 9}
print('3.1:     Set:                     ',my_set)

my_set.update({'3': 6, '4': 5})
delted2 = my_set.pop('1')
print('3.2:     Deleted value2           ',delted2)
print('3.2.2:   Modified set:            ',my_set)