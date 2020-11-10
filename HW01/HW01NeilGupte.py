from random import choice

#this function does error checking for correct input from the user
def user_choice()->str :
    while True:
        check_list:str = ['R', 'P', 'S', 'Q']
        print("\n\nNew Round ------------------------------------------------------------------------>")
        user_input:str= input(str("Please type in your choice \n R for Rock \n P for Paper \n S for Scissors \n Q to Quit "))
        user_input1:str = user_input.upper()
        if user_input1 in check_list:
            return user_input1

#this function converts the choices entered by the users into complete words
def choice_convert(choice :str)->str:
    if choice=="R":
        return "Rock"
    elif choice=="S":
        return "Scissors"
    elif choice=="P":
        return "Paper"
    else:
        return "Quit"

#this function picks random element from the list
def get_computer_move() -> str:
    move: str = choice(['Rock', 'Paper', 'Scissors'])
    return move


#this function uses nested dictionary to save possible scenarios and find out the results
#the nested dictionary has one key for the users choice and the values of this is a nested dictionary having a dictionary all three possible choices of computer.
def game_logic(user_input1 : str) ->None:
    choice_dict: str = {
        "Rock": {"Rock": "\nThe game is Drawn", "Scissors": "\nCongratulations,You win", "Paper": "\nSorry,You lose"},
        "Scissors": {"Scissors": "\nThe game is Drawn", "Paper": "\nCongratulations,You win", "Rock": "\nSorry,You lose"},
        "Paper": {"Paper": "\nThe game is Drawn", "Rock": "\nCongratulations,You win", "Scissors": "\nSorry,You lose"}
    }

    print("\n\n-------------------The GAME has begun------------------------")
    print(f"\nYou have chosen {user_input1}")
    comp_choice:str = get_computer_move()
    print(f"\nThe computer has chosen {comp_choice}")
    print("\nThe final outcome is ------------------>")
    print(choice_dict[user_input1][comp_choice], "\n\n")
    print("\n End of round-------------------------------------------------")




#the main function where all other functions are called
def main()->None:
    while True:
        choice :str =user_choice()
        user_input1: str=choice_convert(choice)
        if user_input1=='Quit':
            break
        else:
            game_logic(user_input1)

if __name__ == '__main__':
    main()
