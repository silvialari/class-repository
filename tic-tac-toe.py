""" Tic Tac Toe impplementation.
    - Computer uses random moves.

Requires: Pyrhon3

Usage:

    python3  [-h] [-s]

   -s  --start-game    Start a Game
"""
import argparse
import os
import random
import time

NONE = "no one"


class TicTacToe():
    """
    Implementation of the TicTacToe game
    """
    def __init__(self):
        """
        Initialize board and available moves
        """
        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]

        self.available_moves = [(0, 0), (0, 1), (0, 2),
                                (1, 0), (1, 1), (1, 2),
                                (2, 0), (2, 1), (2, 2)]

    def print_board(self):
        """
        Clear the screen and display the tic-tac-toe board on screen
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nTic-Tac-Toe\n")

        for index in range(len(self.board)):
            row = abs(len(self.board)-index-1)
            col = 0

            print(f'{row:^3}|{self.board[row][col]:^3}|{self.board[row][col+1]:^3}|{self.board[row][col+2]:^3}|')  # noqa: E501
            print('---+'*4)

        print(f'   |{0:^3}|{1:^3}|{2:^3}|\n\n')

    def computer_move(self, make_move=False):
        """
        If it's computer's move then get the next slot to put on a 'O' in

        :params bool make_move: True if it's the computer's turn
        """
        if not make_move or len(self.available_moves) == 0:
            return

        # make it look like I'm thinking:
        time.sleep(2)
        next_move_index = random.randint(0, len(self.available_moves)-1)
        next_move = self.available_moves[next_move_index]

        x, y = next_move
        self.board[x][y] = 'O'
        self.available_moves.remove((x, y))
        self.print_board()

    def store_user_move(self, x, y):
        """ store the moves and update available moves """
        self.board[x][y] = 'X'
        self.available_moves.remove((x, y))

    def _row_win(self, users):
        """ helper function to determine row winner """
        for user in users.keys():
            winner = [sublist for sublist in self.board if sublist.count(user) == 3]

            if winner:
                print(f'{users[user]} won!!!')
                return True

    def _col_win(self, users):
        """ helper function to determine col winner """
        for col in range(len(self.board[0])):
            if self.board[0][col] == self.board[1][col] and self.board[1][col] == self.board[2][col] and self.board[2][col] != '':  # noqa: E501
                user = self.board[0][col]
                print(f'{users[user]} won!!!')
                return True

    def _diag_win(self, users):
        """ helper function to determine diag winner """
        user = None

        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[1][1] != '' or \
           self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[1][1] != '':      # noqa: E501
            user = self.board[1][1]

        if user:
            print(f'{users[user]} won!!!')
            return True

        return False

    def determine_winner(self):
        """
        Determine who won:
        - if stil avail plays - return False
        - if no avail plays - return None

        :return True if game over
        """
        users = {'X': 'Player', 'O': 'Computer'}

        if len(self.available_moves) == 0:
            print("No Winner")
            return True

        if self._row_win(users):
            return True

        if self._col_win(users):
            return True

        if self._diag_win(users):
            return True

        return False

    def run(self):
        """
        Run the game method
        """
        computer_move = False

        while True:
            self.print_board()
            self.computer_move(make_move=computer_move)

            if self.determine_winner():
                break

            print("Available moves:\n ", self.available_moves, "\n")
            index = input("Please enter a position on the box: (e.g: 0,0) q to exit: ")

            if 'q' in index.lower():
                break

            try:
                x, y = index.split(',')

                if self.board[int(x)][int(y)]:
                    input(f"Position {x},{y} is already taken [Press any key to continue]")
                    computer_move = False
                    continue

                self.store_user_move(int(x), int(y))
                computer_move = True
            except IndexError:
                input("Please enter two numerical values in range 0 to 2 each [Press any key to continue]")  # noqa: E501
                computer_move = False
            except ValueError:
                input("Please enter two numerical values separated by a comma [Press any key to continue]")  # noqa: E501
                computer_move = False


def process_cmd():
    """Process command line arguments. Should have more options like loading old games or asking for a user name"""  # noqa: E501
    parser = argparse.ArgumentParser(description="Tic Tac Toe game")

    parser.add_argument('-s', '--start-game', dest='start', default=False, required=False, action='store_true',  # noqa: E501
                        help='start game')
    parser.set_defaults(start=False)
    return parser.parse_args()


def main():
    """Entry point"""
    game = TicTacToe()
    game.run()


if __name__ == '__main__':
    args = process_cmd()
    if args.start:
        main()

    print("Tic Tac Toe game to start it use the option --start-game when running this script!")
