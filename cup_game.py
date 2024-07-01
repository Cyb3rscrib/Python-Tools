from random import shuffle

#takes a list and shuffle it
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

#accept player guess until its 0,1 or 2
def player_guess():
    guess = ' '

    while guess not in ['0', '1', '2']:
        guess = input("pick a cup: 0,1 or 2\n")

    return int(guess)

#check if the guest is correct
def check_guess(mylist,guess):
    if mylist[guess] == "O":
        print('you won')
    else:
        print('Wrong guess!')
        print(mylist)

#check after every round if the plaer wants to play or not
start_game = "y"
while True:
    if start_game == 'y':
        #initial cup placement
        cup_list = [' ', 'O', ' ']

        #mix list and check if the guest was right or wrong
        check_guess(shuffle_list(cup_list),player_guess())
        start_game = input('do you want to play?(y / n): ')

    elif start_game == 'n':
        print('Bye Bye')
        break
    else:
        start_game = input('do you want to play again?(y / n): ')