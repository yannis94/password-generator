import random

def generatePWD(nbrChar, nbrNum, nbrSymb):
    password = ''
    char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digit = '0123456789'
    symb = '&$.?*%!@_-+|~'
    for i in range(int(nbrChar)):
        randI = random.randint(0, len(char) - 1)
        password += char[randI]
    for i in range(int(nbrNum)):
        randI = random.randint(0, len(digit) - 1)
        password += digit[randI]
    for i in range(int(nbrSymb)):
        randI = random.randint(0, len(symb) - 1)
        password += symb[randI]

    return ''.join(random.sample(password, len(password)))

print('---------- Secret key Generator ----------\n\n')
letterNbr = input('How many letters: ')
digitNbr = input('How many digit: ')
symbNbr = input('How many symbols: ')
generatorNbr = input('How many key you want: ')
print('\nGenerating ...\n\n')

for x in range(int(generatorNbr)):
    print(generatePWD(letterNbr, digitNbr, symbNbr))

print('\nDone.')
