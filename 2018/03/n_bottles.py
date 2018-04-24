def bottles(n):
    """Formats plural according to number of bottles."""
    return ('1 bottle' if n == 1 else str(n) + ' bottles') + ' of beer'

def n_bottles(n):
    """
    Go through the bottles of beer on the wall, and pass them around.

    Calls `bottles(n)` for formatting, and reduces n by 1 each iteration
    """
    if 5 <= n <= 99:
        while(n > 0):
            print(bottles(n) + ' on the wall,\n  ' + bottles(n) + '.')
            n = n - 1
            print('Take one down and pass it around,\n  ' +
                # conditional expression to determine whethere there are bottles left
                bottles(n if n > 0 else 'no more') + 
                ' on the wall.\n')
    else:
        print('I want to sing funnier songs than "' + bottles(n) + '".\n')


n_bottles(3)
n_bottles(1011)
n_bottles(9)
