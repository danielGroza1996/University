'''
Generate the smallest perfect number larger than a given natural number.
'''

def readNumber():
    '''
    Reads a natural number from the keyboard.
    INPUT: None
    OUTPUT: number - the read natural number
    '''
    number = int(input('Number: '))
    return number

def getSumOfDivisors(number):
    '''
    Returns the sum of the divisors of the input number (except the number itself).
    INPUT: number - a natural number
    OUTPUT: ssum - the sum of the divisors of the input number 
    '''
    if number == 0:
        return float('inf')
    ssum = 1
    for counter in range(2, number//2+1):
        if number % counter == 0:
            ssum = ssum + counter
    return ssum
    
def isPerfect(number):
    '''
    Checks whether the input number is perfect.
    INPUT: number - a natural number
    OUTPUT: True if the input number is perfect, False otherwise
    '''
    if number == 1:
        return False
    return getSumOfDivisors(number) == number

def getFirstPerfectNumberLargerThan(number):
    '''
    Returns the first perfect number larger than the input number.
    INPUT: number - a natural number
    OUTPUT: perfect - first perfect number larger than the input number
    '''
    perfect = number + 1
    while not isPerfect(perfect):
        perfect = perfect + 1
    return perfect

def main():
    '''
    Program Entry Point
    NOTE! This program does NOT contain input data validation!
    '''
    number = readNumber()
    print('The smallest perfect number larger than ' + str(number) + ' is ' + str(getFirstPerfectNumberLargerThan(number)))
    
main()