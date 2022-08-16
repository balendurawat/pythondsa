# convert a number from decimal to binary using recursion
# 1) the flow:
    # 1) divide the number by 2
    # 2) get the integer quotient for the next generation
    # 3) get the remainder for the binary digit 
    # 4) repeat the steps
# recursive function : f(n) = n mod 2 + 10 * f(n/2)


def decimalToBinary(n):
    assert int(n) == n, 'The parameter must be an integer only'
    if n == 0:
        return 0
    else:
        return n%2 + decimalToBinary(int(n/2))

print(decimalToBinary(1.2))
