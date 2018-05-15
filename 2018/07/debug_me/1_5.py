def calc(a,b,operation):
    """
    returns the product of a and b if operation is 'product'
    returns the sum of a and b in any other case
    """

    if operation == 'product':
        return a * b
    else:
        return a + b

print(calc('product',3,5))
