from datetime import datetime
import pytz

# Get the timezone object for Tokyo
tz_TK = pytz.timezone('Asia/Tokyo')

# Get the current time in Tokyo
datetime_TK = datetime.now(tz_TK)

# Format the time as a string and print it
print("Game was run at:", datetime_TK.strftime("%H:%M:%S"))

##### START GAME CODE ######
choice_map = {"7": 0, "8": 1, "9": 2, "4": 3, "5": 4, "6": 5, "1": 6, "2": 7, "3": 8}

board_keys = ["7", "8", "9", "4", "5", "6", "1", "2", "3"]


def display_board(game_board):
    print("        |       |")
    print("    " + game_board[0] + "   |   " + game_board[1] + "   |   " + game_board[2])
    print("  ______|_______|______")
    print("        |       |")
    print("    " + game_board[3] + "   |   " + game_board[4] + "   |   " + game_board[5])
    print("  ______|_______|______")
    print("        |       |")
    print("    " + game_board[6] + "   |   " + game_board[7] + "   |   " + game_board[8])
    print("        |       |")
    print('\n')


def check_for_winner(game_board):
    # check if 7,5,3 or 1,5,9 or 7,8,9 or 4,5,6 or 1,2,3 are all X or O
    check_h1 = game_board[0:3]
    check_h2 = game_board[3:6]
    check_h3 = game_board[6:9]
    check_v1 = [game_board[0], game_board[3], game_board[6]]
    check_v2 = [game_board[1], game_board[4], game_board[7]]
    check_v3 = [game_board[2], game_board[5], game_board[8]]
    check_d1 = [game_board[0], game_board[4], game_board[8]]
    check_d2 = [game_board[6], game_board[4], game_board[2]]
    all_scenarios = [check_h1, check_h2, check_h3, check_v1, check_v2, check_v3, check_d1, check_d2]

    for element in all_scenarios:
        # print(element)
        if len(set(element)) == 1 and set(element).pop() != ' ':
            print(f'\n WINNER ! ! ! ! \n')
            return True

    return False


# keeps track of which player's turn
def player_turn(turn):
    if turn % 2 == 0:
        return "Two '[O]'"
    else:
        return "One '[X]'"


def check_free_square(index, game_board):
    if index not in choice_map.keys():
        return True
    elif game_board[choice_map[index]] == " ":
        return True
    else:
        return False


def player_input(turn, game_board):
    choice = None
    # valid inputs the player can choose
    valid = ["7", "8", "9", "4", "5", "6", "1", "2", "3"]

    while choice not in valid and check_free_square(choice, game_board):
        choice = input(f'Player {player_turn(turn)}: Pick your Square: ')
        print('\n')
        if choice not in valid:
            print('Invalid option, try again.')
        if not check_free_square(choice, game_board):
            print('Square already taken, please choose again. \n')
            choice = None

    if turn % 2 == 0:
        game_board[choice_map[choice]] = 'O'
    else:
        game_board[choice_map[choice]] = 'X'

    display_board(game_board)


def play_again(game_board):
    answer = input('Do you want to play again?   Y or N: ')
    if answer.lower() == 'y' or answer.lower() == 'yes' or answer.lower() == 'ok':
        print('\n' * 3)
        return game_play()
    else:
        print('\n Okay Goodbye Dork! \n')


def game_play():
    active_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    winner = False
    turn = 1
    print("\n Game Starting, Let's Gooo!! \n")
    display_board(active_board)

    # while there is not a winner, hence winner is false
    while not winner and turn < 11:

        if turn == 10:
            print('\n Game is Drawn ! ! ! \n')
            turn += 1
            # Check if they want to Play again and re-run game
            play_again(active_board)

        else:
            player_input(turn, active_board)
            winner = check_for_winner(active_board)
            turn += 1

            if turn < 10 and not winner:
                print(f' Round number: {turn}')

            if winner:
                print(f'\n Game Over,  Player {player_turn(turn - 1)} wins, good job Dufus! \n')
                play_again(active_board)

game_play()