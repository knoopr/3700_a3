#!/usr/bin/python
import sys;
from Board import Board;
from copy import deepcopy;
from Node import Node

class AI_player():

    def __init__(self):
        board = str(Board(sys.argv[1])).split("\n")
        self.depth = 4  #even number for max odd for min
        
        #Setting up current player and opponent
        self.player = "B"
        self.opponent = "R"
        for line in board:
            if "Red" in line:
                self.player = "R"
                self.opponent = "B"
    
        self.board = board[3:]

        next_Move = Node(self.board, self.player, self.opponent, self.depth, self.depth,(None, -sys.maxint), (None, sys.maxint)).Get_move(0)
        self.Make_move(next_Move[0])
        

    #Write to move file.
    def Make_move(self, move):
        fp = open( sys.argv[2], "w" );
        fp.write( "%d\n" % move );
        fp.close();




if __name__ == "__main__":
    AI_player()