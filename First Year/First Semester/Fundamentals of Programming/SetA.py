'''
Generate the first prime number larger than a given natural number.
'''

def readNumber():
    '''
    Reads a natural number from the keyboard.
    INPUT: None
    OUTPUT: number - the read natural number
    '''
    number = int(input('Number: '))
    return number

def isPrime(number):
    '''
    Checks whether the input number is prime.
    INPUT: number - a natural number
    OUTPUT: True if the input number is prime, False otherwise 
    '''
    if number == 0 or number == 1:
        return False
    if number == 2:
        return True
    for counter in range(2, number//2+1):
        if number % counter == 0:
            return False
    return True

def getFirstPrimeNumberLargerThan(number):
    '''
    Returns the first prime number larger than the input number.
    INPUT: number - a natural number
    OUTPUT: prime - first prime number larger than the input number
    '''
    prime = number + 1
    while not isPrime(prime):
        prime = prime + 1
    return prime

def main():
    '''
    Program Entry Point
    NOTE! This program does NOT contain input data validation!
    '''
    number = readNumber()
    print('First prime number larger than ' + str(number) + ' is ' + str(getFirstPrimeNumberLargerThan(number)))
    
main()