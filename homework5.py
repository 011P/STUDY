immutable_var = [4, 3.2], True, False, 'Hello'
print(immutable_var)

immutable_var[0][1] = 1
#immutable_var[1] = 0
print(immutable_var)

#тип данных 'tuple' не поддерживает назначение элемента,
#но поддерживает изменение изменяемых элементов внутри него, т. к. списки.

mutable_list = [[6, 5], 3.1, True, 'Hello']
mutable_list[0][1] = 1
mutable_list[0][0] = 2
print(mutable_list)