import sys

def print_squares(n):
    if n > 0:
        print('+' + '--------' + '--+')
        print('|' + '        ' + '  |')
        print('|' + '        ' + '  |' + ('--+' if n > 1 else ''))
        print('|' + '        ' + '  |' + ('  |' if n > 1 else ''))
    for i in range(0, n):
        print('   ' * i + '|' + '        ' + '  |' + ('  |' if i < n - 1 else '') + ('--+' if i < n - 2 else ''))
        print('   ' * i + '+' + '--------' + '--+' + ('  |' if i < n - 1 else '') + ('  |' if i < n - 2 else ''))

if __name__ == "__main__":
    try:
        n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
        if n < 0:
            raise ValueError
    except (ValueError, IndexError):
        print("Usage: python3 squares.py [n] (where n is a positive integer)")
        sys.exit(1)
    print_squares(n)
