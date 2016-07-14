"""
Python
reference:
https://github.com/step16/hw7/blob/master/python/main.py //Copyright 2007 Google Inc.
"""


import copy
import json
import webapp2
import random


class OthelloBoard:
    """
    getting json data of the othello board and provide an interface
    """
    def __init__(self, body):
        """
        get json data from: http://step-othello.appspot.com
        return a dict
        { "board":{"Pieces":...,"Next":...}, ... , "valid_moves": [dict array] }
        """
        self._board = json.loads(body)

    def board_object(self):
        """
        return underlying board object (dict)
        """
        return self._board

    def piece_position(self, col, row):
        """
        return: piece on the board (integer: 0, 1, or 2)
        0 for no pieces, 1 for player 1, 2 for player 2
        example "board" variable in piece_position(board,...)
        [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,2,0,0,0],
        [0,0,1,1,2,0,0,0],
        [0,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
        save in self.board_["board"]["Pieces"]
        """
        return piece_position(self._board["board"]["Pieces"], col, row)

    def next_player(self):
        """
        return: integer (1 or 2)
        show who play next (current playing)
        {"board":{"Pieces":...
        ,"Next":2}...}
        """
        return self._board["board"]["Next"]

    def valid_moves(self):
        """
        return an array (valid move for the next player
        each move is a dict {"Where": [x,y],"As": player number}
        example:
        [{"Where":[2,4],"As":2},{"Where":[3,5],"As":2},{"Where":[3,6],"As":2}]
        save in self.board_["valid_moves"]
        """
        if self._board["valid_moves"]:
            return self._board["valid_moves"]
        return []

    def __update_board_direction(self, new_board, col, row, delta_x, delta_y):
        """
        helper function of next_board_position
        It looks towards (delta_x, delta_y) direction and flip if valid.
        It looks towards (delta_x, delta_y) direction and flip if valid.
        x direction: column
        y direction: row
        """
        player = self.next_player()
        opponent = 3 - player
        look_x = col + delta_x
        look_y = row + delta_y
        flip_list = []
        while piece_position(new_board, look_x, look_y) == opponent:
            flip_list.append([look_x, look_y])
            look_x += delta_x
            look_y += delta_y
        if piece_position(new_board, look_x, look_y) == player:
            set_piece(new_board, col, row, player)
            for flip_move in flip_list:
                flip_x = flip_move[0]
                flip_y = flip_move[1]
                set_piece(new_board, flip_x, flip_y, player)

    def next_board_position(self, move):
        """
        return board positions after a move dict
        return None if the move itself is invalid.
        """
        if move not in self.valid_moves():
            return None
        col = move["Where"][0]
        row = move["Where"][1]
        new_board = copy.deepcopy(self._board["board"]["Pieces"])
        self.__update_board_direction(new_board, col, row, 1, 0)
        self.__update_board_direction(new_board, col, row, 0, 1)
        self.__update_board_direction(new_board, col, row, -1, 0)
        self.__update_board_direction(new_board, col, row, 0, -1)
        self.__update_board_direction(new_board, col, row, 1, 1)
        self.__update_board_direction(new_board, col, row, -1, 1)
        self.__update_board_direction(new_board, col, row, 1, -1)
        self.__update_board_direction(new_board, col, row, -1, -1)
        return new_board


# global functions used in OthelloBoard class:
def piece_position(board, col, row):
    """
    board: 8 * 8 matrix
    col: A ~ H (1 ~ 8)
    row: 1 ~ 8
    matrix number order:
    matrix[0 ~ 7][0 ~ 7]
    """
    if 1 <= col <= 8 and 1 <= row <= 8:
        return board[row - 1][col - 1]
    return None


# Set piece on the board at (x,y) coordinate
def set_piece(board, col, row, piece):
    if col < 1 or 8 < col or row < 1 or 8 < row or piece not in [0, 1, 2]:
        return False
    board[row - 1][col - 1] = piece


# Debug function to pretty print the array representation of board.
def pretty_print(board, nl="<br>"):
    s = ""
    for row in board:
        for piece in row:
            s += str(piece)
        s += nl
    return s


def parse_move(move):
    """
    valid move = [{"Where":[2,4],"As":2},{"Where":[3,5],"As":2},{"Where":[3,6],"As":2}]
    col -> A  ~ H
    row -> 1 ~ 8
    return the position on the board
    """
    m = move["Where"]
    return '%s%d' % (chr(ord('A') + m[0] - 1), m[1])


class Test(webapp2.RequestHandler):
    """
    Handling GET request, just for debugging purposes.
    If you open this handler directly,
    it will show you the HTML form here and let you copy-paste some game's JSON
    * for testing *
    """
    def get(self):
        if not self.request.get('json'):
            self.response.write("""
            <title>JSON Game Tester - Stephanie</title>
            <body><form method=get>
            Paste JSON here:<p/><textarea name=json cols=80 rows=24></textarea>
            <p/><input type=submit>
            </form>
            </body>
            """)
            return
        else:
            g = OthelloBoard(self.request.get('json'))
            self.determine_move(g)

    def post(self):
        """
        Reads JSON representation of the board and store as the object.
        picking of a move and print the result.
        """
        game = OthelloBoard(self.request.body)
        self.determine_move(game)

    def determine_move(self, game):
        """
        determine the move from all valid moves
        if no valid move then pass the game
        """
        valid_moves = game.valid_moves()
        if len(valid_moves) == 0:
            self.response.write("PASS")
        else:
            # move = self.random_move(game) # method 1: move randomly
            move = self.next_best_board(game)  # method 2: move to get better next board
            self.response.write(parse_move(move))

    # methods to determine the next move:
    def random_move(self, game):
        """
        randomly pick a move from all the valid move
        """
        move = random.choice(game.valid_moves())
        return move

    def next_best_board(self, game):
        """
        choose a move that will result in performing the best next board
        """
        player1 = {}
        player2 = {}
        for move in game.valid_moves():
            next_board = game.next_board_position(move)
            score = self.board_score(next_board)  # return a tuple
            player1[score[0]] = move
            player2[score[1]] = move
        if game.next_player() == 1:  # player1 is playing
            best_score = max(player1)
            return player1[best_score]
        else:
            best_score = max(player2)
            return player2[best_score]

    def board_score(self, board):
        """
        helper function of next_best_board
        """
        score_player1 = 0
        score_player2 = 0
        for row in board:
            for piece in row:
                if piece == 1:
                    score_player1 += 1
                elif piece == 2:
                    score_player2 += 1
                else:
                    continue
        return score_player1, score_player2

    def min_max(self):
        pass


app = webapp2.WSGIApplication([
    ('/', Test)
], debug=True)
