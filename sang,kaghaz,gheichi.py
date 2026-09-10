from random import randint



player_score = 0
computer_score = 0

rounds = int(input('enter rounds: '))
for i in range(rounds):

    player_choice = int(input("(sang = 1, kaghaz = 2, gheichi = 3) choice :"))
    computer_choice = randint(1,3)

    if player_choice == 1:
        print("your choice : sang")
    elif player_choice == 2:
        print("your choice : kaghaz")
    elif player_choice == 3:
        print("your choice : gheichi")
    else:
        print("your choice : invalid")


    if computer_choice == 1:
        print("computer choice : sang")
    elif computer_choice == 2:
        print("computer choice : kaghaz")
    elif computer_choice == 3:
        print("computer choice : gheichi")



    if player_choice == computer_choice:
        print("mosavi")

    elif(player_choice == 1 and computer_choice == 3) or\
        (player_choice == 2 and computer_choice == 1)or\
        (player_choice == 3 and computer_choice == 2):

        print("you win")
        player_score += 1

    else:
        print("computer win")
        computer_score += 1

rounds -= 1

print("\n===============================")
print(f"your last score : {player_score} | computer last score : {computer_score}")

if player_score > computer_score:
    print("you win the game")

elif computer_score > player_score:
    print("computer win the game")

else:
    print("mosavi")



