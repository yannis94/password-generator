def getIntro():
    print('---------- Secret key Generator ----------\n\n')
    print('Make your choice :\n')
    print('[1] hash / password')
    print('[2] passphrase')
    
    userChoice = 0
    correctInput = False

    while correctInput is False:
        testValue = input('Choice > ')
        try:
            int(testValue)
        except ValueError:
            print('You should type a number')
        else:
            testValue = int(testValue)
            if testValue == 1 or testValue == 2:
                userChoice = testValue
                correctInput = True
            else:
                print('This choice doesn\'t exist')

    return userChoice
