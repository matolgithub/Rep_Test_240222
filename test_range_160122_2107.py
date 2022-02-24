x = input('enter something: ')
if x.isdigit():
    print('You enter digits')
elif x.isalpha():
    print('You enter simbols')
else:
    print('You enter something!')
print(x, type(x))
print(x[0:4])
print(x[::-1])
print(x[::])