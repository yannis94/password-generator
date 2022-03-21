import random 

def askInt(question):
    result = 0
    correctValue = False
    while correctValue == False:
        userInput = input(question)
        try:
            int(userInput)
        except ValueError:
            print('You should enter a number')
        else:
            correctValue = True
            result = int(userInput)

    return result
            

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

def hash():
    letterNbr = askInt('How many letters: ')
    digitNbr = askInt('How many digit: ')
    symbNbr = askInt('How many symbols: ')
    generatorNbr = askInt('How many key you want: ')
    print('\nGenerating ...\n\n')

    for x in range(int(generatorNbr)):
        print(generatePWD(letterNbr, digitNbr, symbNbr))
