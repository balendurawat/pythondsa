
def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    else:
        return base * power(base, exponent-1)
    
    
power(2,4)