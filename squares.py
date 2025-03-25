def print_squares(n):
    if n > 0:
        print('+' + '--------' + '--+')
        print('|' + '        ' + '  |')
        print('|' + '        ' + '  |' + ('--+' if n > 1 else ''))
        print('|' + '        ' + '  |' + ('  |' if n > 1 else ''))
    for i in range(0, n):
        print('   ' * i + '|' + '        ' + '  |' + ('  |' if i < n - 1 else '') + ('--+' if i < n - 2 else ''))
        print('   ' * i + '+' + '--------' + '--+' + ('  |' if i < n - 1 else '') + ('  |' if i < n - 2 else ''))

for i in range(0, 10):
    print(i, ':')
    print_squares(i)
    print('')