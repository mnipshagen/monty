def calc(a,b,operation):
    '''
    Performs a multiplication or summation on two values a and b

    Args:
        a: First value
        b: Second value
        operation: Operation to be performed on the values

    Return:
        a * b if operation was specified as 'product', otherwise a + b
    '''

    if operation == 'product':
        return a * b
    else:
        return a + b

# arguments were given in the wrong order. operation goes last
print(calc(3,5,'product'))
