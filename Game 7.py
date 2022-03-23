# Game Rules
print("*Game Rules*")
print("1.Input number of coins.")
print("2.Input a non-zero squared number to remove from coins.")
print("3.The player who removes the last coin wins.")
# Take number of coins from user
coins = int(input("please enter number of coins: "))
# check if coins not smaller than or equal zero
while coins <= 0:
    print("invalid number, please enter another number: ", end='')
    coins = int(input())
while True:
    # for loop to switch between two players
    for player in [1, 2]:
        number = int(input("player " + str(player) + " , please enter a number: "))
        square_root = number ** 0.5
        modulus_1 = square_root % 1
        # check if number doesn't have square root and not equal zero or bigger than coins
        while modulus_1 != 0 or number == 0 or number > coins:
            print("invalid number, please enter another number: ", end='')
            number = int(input())
            square_root = number ** 0.5
            modulus_1 = square_root % 1
        if modulus_1 == 0 and number <= coins:
            # remove number from coins and print remaining coins
            coins = coins - number
            print("remaining coins = " + str(coins))
        # check if there is a winner
        if coins == 0:
            print("player " + str(player) + " wins!!")
            exit()
