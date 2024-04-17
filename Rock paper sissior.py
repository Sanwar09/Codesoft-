import random
def det_winner(uchoice, cchoice):
    if uchoice == cchoice:
        return "It's a tie!"
    elif (uchoice == 'rock' and cchoice == 'scissors') or \
         (uchoice == 'scissors' and cchoice == 'paper') or \
         (uchoice == 'paper' and cchoice == 'rock'):
        return "You win the game 🥳🥳🥳!"
    else:
        return "You Lose The Game 🥲🥲🥹!"

uscore = 0
cscore = 0
choices = ['rock', 'paper', 'scissors']

print('''Welcome to Rock, Paper, Scissors Game!
         Best of Luck for the Game👍👍
         ''')

while True:
    uchoice = input("\nChoose rock, paper, or scissors (or 'q' to exit): ").lower()

    if uchoice == 'q':
        print("Thanks for playing!")
        break

    if uchoice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    cchoice = random.choice(choices)

    print(f"\nYou chose: {uchoice}")
    print(f"Computer chose: {cchoice}")

    result = det_winner(uchoice, cchoice)
    print(result)

    if result == "You win the game 🥳🥳🥳!":
        uscore += 1
    elif result == "You Lose The Game 🥲🥲🥹!":
        cscore += 1

    print(f"Score - You: {uscore}, Computer: {cscore}")
