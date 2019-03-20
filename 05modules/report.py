def get_description():
    '''
    Returns weather forecast
    '''
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)

def add(x, y):
    """
    Add x and y
    >>> add(2, 3)
    5
    """
    return x + y