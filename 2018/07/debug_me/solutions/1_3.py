# colon at the end of the line was missing
def get_max(a,b):
    '''
    Returns the bigger of two values

    Args:
        a: First value
        b: Second value

    Return:
        a if a > b, else b
    '''

    if a > b:
        return a
    else:
        return b

print(get_max(7,3))
