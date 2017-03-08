class ArgumentError(ValueError): pass

def f(num):
    if num < 0:
        raise ArgumentError('should be non-negative')
    
    if num == 0:
        return 1

    return num * f(num - 1)
