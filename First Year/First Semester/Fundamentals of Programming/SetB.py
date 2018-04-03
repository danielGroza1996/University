'''
Determine the product of all the proper factors of a given natural number.
'''

def readNumber():
    '''
    Reads a natural number from the keyboard.
    INPUT: None
    OUTPUT: number - the read natural number
    '''
    number = int(input('Number: '))
    return number

def getProperFactors(number):
    '''
    Returns an iterable containing the proper factors of the input number.
    INPUT: number - a natural number
    OUTPUT: factors - proper factors of the input number
    '''
    factors = []
    for counter in range(2, number//2+1):
        if number % counter == 0:
            factors.append(counter)
    return factors

def getProductOfIterable(iterable):
    '''
    Returns the product of the input iterable.
    INPUT: iterable - an iterable of natural numbers
    OUTPUT: product - the product of the input iterable
    '''
    if len(iterable) == 0:
        return 0
    product = 1
    for element in iterable:
        product = product * element
    return product

def main():
    '''
    Program Entry Point
    NOTE! This program does NOT contain input data validation!
    '''
    number = readNumber()
    print('The product of all the proper factors of ' + str(number) + ' is ' + str(getProductOfIterable(getProperFactors(number))))
    
main()