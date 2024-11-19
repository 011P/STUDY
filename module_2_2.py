a = int(input('first num: '))
b = int(input('second num: '))
c = int(input('third num: '))
x = [a, b, c]

if a == b and a == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
else:
    print(0)
