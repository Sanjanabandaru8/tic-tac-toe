#tic-tac-toe game

import random





def print_board(board):
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()



def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    if ' ' not in board:
        return 'Tie'
    return False



def computer_move(board):

     # Check if player can win in the next move
    winning_moves = []
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_win(board) == 'X':
                winning_moves.append(i)
            board[i] = ' '

    # If player can win, block their winning move with 80% probability
    if winning_moves:
        if random.random() < 0.8:
            board[random.choice(winning_moves)] = 'O'
        else:
            # Make a random move
            available_moves = [i for i, x in enumerate(board) if x == ' ']
            board[random.choice(available_moves)] = 'O'
    else:
        # Make a random move
        available_moves = [i for i, x in enumerate(board) if x == ' ']
        board[random.choice(available_moves)] = 'O'


def single_player_game():
    board = [' ' for _ in range(9)]
    print("You play as X, computer plays as O.")
    while True:
        print_board(board)
        while True:
            move = input("Enter your move (1-9): ")
            if move.isdigit() and 1 <= int(move) <= 9:
                move = int(move) - 1
                if board[move] == ' ':
                    board[move] = 'X'
                    break
                else:
                    print("Invalid move, space already occupied.")
            else:
                print("Invalid move, please enter a number between 1 and 9.")
        result = check_win(board)
        if result:
            print_board(board)
            if result == 'Tie':
                print("It's a tie!")
            elif result == 'X':
                print("You win!")
            else:
                print("Computer wins!")
            break
        computer_move(board)
        result = check_win(board)
        if result:
            print_board(board)
            if result == 'Tie':
                print("It's a tie!")
            elif result == 'X':
                print("You win!")
            else:
                print("Computer wins!")
            break





def two_player_game():
    board = [' ' for _ in range(9)]
    current_player = 'X'
    while True:
        print_board(board)
        move = input("Player {}, enter your move (1-9): ".format(current_player))
        if board[int(move) - 1] == ' ':
            board[int(move) - 1] = current_player
            result = check_win(board)
            if result:
                print_board(board)
                if result == 'Tie':
                    print("It's a tie!")
                else:
                    print("Player {} wins!".format(result))
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move, try again.")




def main():
    while True:
        print("Tic Tac Toe Menu:")
        print("1. Single Player (against computer)")
        print("2. Two Player")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            single_player_game()
        elif choice == "2":
            two_player_game()
        elif choice == "3":
            break
        else:
            print("Invalid choice, try again.")




if __name__ == '__main__':
    main()