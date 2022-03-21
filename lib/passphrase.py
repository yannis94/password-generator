import random

def askNumber():
    isCorrect = False
    result = 0

    while isCorrect == False:
        userInput = input('How many passphrase do you want > ')

        try:
            int(userInput)
        except ValueError:
            print('You should enter a number')
        else:
            isCorrect = True
            result = int(userInput)

    return result

def getList():
    words = []
    with open('wordslist.txt', 'r', encoding='utf8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace('\n', '')
            words.append(line)
    
    return words

def generatePassphrase(words):
    words_list = getList()
    words_picked = []
    for i in range(words):
        randI = random.randint(0, len(words_list) - 1)
        words_picked.append(words_list[randI])

    return '-'.join(words_picked)

def getPassphrase():
    print('>>>>> Passphrase <<<<<\n')
    num = askNumber()
    userChoice = ''
    while isinstance(userChoice, int) == False:
        words_number = input('How many words > ')
        try:
            int(words_number)
        except ValueError:
            print('You should input a number')
        else:
            userChoice = int(words_number)

    print('\n')

    for i in range(num):
       print(generatePassphrase(userChoice))

