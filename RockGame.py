import random


while True:
      
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    player = None


    while player not in choices:
        player = input('Enter: rock, paper or scissors: ').lower()

    if player == computer:
        print('computer', computer)
        print('player', player)
        print("Ohh that's tie")
    elif player == 'rock':
        if computer == 'paper':
                print('computer', computer)
                print('player', player)
                print("You lose")
        if computer == 'scissors':
                print('computer', computer)
                print('player', player)
                print("You won")


                
    elif player == 'scissors':
        if computer == 'paper':
                print('computer', computer)
                print('player', player)
                print("You lose")
        if computer == 'rock':
                print('computer', computer)
                print('player', player)
                print("You won")



    elif player == 'paper':
        if computer == 'scissors':
                print('computer', computer)
                print('player', player)
                print("You won")
        if computer == 'rock':
                print('computer', computer)
                print('player', player)
                print("You lose")

    playAgain = input('Wanna play again (Yes/No): ').lower()
    if playAgain != 'yes':
          break

print('bye')