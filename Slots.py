import random
import pickle

# number of units the user has to bet with
playerCash = [100]
playerCash = pickle.load(open('units.txt', 'rb'))
machineCash = [5000]

# starts the program when opened
def startUp(CASH):
    print("\nThank you for playing this slot machine. "
           "Please play responsibly.")

    spinStart()

# Start of reel spin
def spinStart():
    userChoice = input("\nWould you like to spin the reel? (Reply with 'yes' or 'no'.\n"
                       ">>")

    if userChoice in ['yes', 'Yes']:
        spinMain(playerCash, machineCash)
    elif userChoice in ['no', 'No']:
        print("Why would you open a slot machine program if you weren't going "
              "to spin the reel?")
        exit()
    else:
        print("You did not reply with a valid response.")
        spinStart()

def spinMain(CASH, MCASH):
    print("\n---You have", CASH[0], "units.---")
    betAmount = int(input("\nHow many units would you like to bet?\n"
                           "Please enter a whole number.\n"
                           ">>"))
    if CASH[0] <= 0:
        print("\nYou are out of units :(.")
    elif CASH[0] < betAmount:
        print("\nYou cannot bet more units than you own!")
        spinMain(playerCash, machineCash)
    else:
        CASH[0] = CASH[0] - betAmount

        # save cash amount to txt file
        pickle.dump(CASH, open('units.txt', 'wb'))

        print(CASH[0])
        print("\nSpinning reel...")

        # TODO make this a loop
        reelSpot1 = random.randint(1,4)
        if reelSpot1 == 1:
            reelItem1 = "|Cherries|"
        elif reelSpot1 == 2:
            reelItem1 = "|Apples|"
        elif reelSpot1 == 3:
            reelItem1 = "|Lemons|"
        elif reelSpot1 == 4:
            reelItem1 = "|Bomb|"

        reelSpot2 = random.randint(1, 4)
        if reelSpot2 == 1:
            reelItem2 = "|Cherries|"
        elif reelSpot2 == 2:
            reelItem2 = "|Apples|"
        elif reelSpot2 == 3:
            reelItem2 = "|Lemons|"
        elif reelSpot2 == 4:
            reelItem2 = "|Bomb|"

        reelSpot3 = random.randint(1, 4)
        if reelSpot3 == 1:
            reelItem3 = "|Cherries|"
        elif reelSpot3 == 2:
            reelItem3 = "|Apples|"
        elif reelSpot3 == 3:
            reelItem3 = "|Lemons|"
        elif reelSpot3 == 4:
            reelItem3 = "|Bomb|"

        reelSpot4 = random.randint(1, 4)
        if reelSpot4 == 1:
            reelItem4 = "|Cherries|"
        elif reelSpot4 == 2:
            reelItem4 = "|Apples|"
        elif reelSpot4 == 3:
            reelItem4 = "|Lemons|"
        elif reelSpot4 == 4:
            reelItem4 = "|Bomb|"

        # this is for win deciding
        allReel = reelSpot1, reelSpot2, reelSpot3, reelSpot4
        print(str(allReel))
        print(reelItem1, reelItem2, reelItem3, reelItem4)
        if allReel in [(1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3)]:
            print("Winner!")
        elif allReel in [4]:
            print("Boo, you lost!")
        else:
            print("Boo, you lost!")

        spinStart()

startUp(playerCash)