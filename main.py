from lib.showIntro import getIntro 
from lib.hash import hash 
from lib.passphrase import getPassphrase 

choice = getIntro()
if choice == 1:
    hash()
elif choice == 2:
    getPassphrase()

print('\n\nDone.')
