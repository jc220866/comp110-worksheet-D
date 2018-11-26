class OxoBoard:
    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """
        # Lists are simple to call and easily mutable.
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        # We initialize current turn to player 1 and change it after every turn
        self.current_turn = 1

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        return self.board[y * 3 + x]

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """

        if self.board[y * 3 + x] == 0:
            self.board[y * 3 + x] = mark

            self.current_turn = mark

            return True

        else:
            return False

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """

        if 0 in self.board:
            return False
        else:
            return True

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """

        # pointers are used to increase readability
        b = self.board
        t = self.current_turn

        # Row - Top
        # Row - Middle
        # Row - Bottom
        # Column - Left
        # Column - Middle
        # Column - Right
        # Diagonal - TopLeft to BottomRight
        # Diagonal - TopRight to BottomLeft

        if (b[0] == t and b[1] == t and b[2]) or \
            (b[3] == t and b[4] == t and b[5]) or \
            (b[6] == t and b[7] == t and b[8]) or \
            (b[0] == t and b[3] == t and b[6]) or \
            (b[1] == t and b[4] == t and b[7]) or \
            (b[2] == t and b[5] == t and b[8]) or \
            (b[0] == t and b[4] == t and b[8]) or \
                (b[2] == t and b[4] == t and b[6]):

            return self.current_turn

        else:
            return 0

    def show(self):
        """ Display the current board state in the terminal. You should not need to edit this. """
        for y in range(3):
            if y > 0:
                print("--+---+--")
            for x in range(3):
                if x > 0:
                    print('|',)

                # Print a space for empty (0), an O for player 1, or an X for player 2
                print(" OX"[self.get_square(x, y)],)
            print
