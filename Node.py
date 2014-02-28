import sys
from copy import deepcopy

class Node():
    def __init__(self,given_Board, the_Player, the_Opponent, goal_Depth, root_Depth, given_Alpha, given_Beta):
        self.board = given_Board
        self.player = the_Player
        self.opponent = the_Opponent
        self.depth = goal_Depth
        self.root = root_Depth
        self.possible_Moves = []
        self.max_Score = (0,0)
        self.worst_Score = (0,0)
        self.alpha = given_Alpha
        self.beta = given_Beta
    
    





    #Return value as 100 or 0
    def Get_move(self, scoring_Method = 0):
        
        if scoring_Method == 1:
            self.score = self.Score_easy
        else:
            self.score = self.Score_hard
        
    
        #If the look ahead depth is not reached compare the value of each branch node
        if self.depth != 0:
            if self.score() == -100 or self.score() == 100:
                return (None, self.score())
            else:
                self.Place_pieces()
            

        
            # Return Max
            if self.depth%2 == 0:
                for i in self.possible_Moves:
                    resultant_Score = Node(i[1], self.player, self.opponent, self.depth - 1, self.root, self.alpha, self.beta).Get_move(scoring_Method)
                    if resultant_Score[1] != None and resultant_Score[1] > self.alpha[1]:
                        self.alpha = (i[0], resultant_Score[1])
                        if self.beta[1] < self.alpha[1]:
                            break
                return self.alpha
            
            
            #Return Min
            elif self.depth%2 == 1:
                for i in self.possible_Moves:
                    resultant_Score = Node(i[1], self.player, self.opponent, self.depth - 1, self.root, self.alpha, self.beta).Get_move(scoring_Method)
                    if resultant_Score[1] != None and resultant_Score[1] < self.beta[1]:
                        self.beta = (i[0], resultant_Score[1])
                        if self.beta[1] < self.alpha[1]:
                            break
                return self.beta
    
    
    
        #If the look ahead depth is reached return the score of each node
        elif self.depth == 0:
            return (None, self.score())



    #First return function 100 if win -100 if loss
    def Score_easy(self):
        self.score_Values = (0,0,0,100)
        
        veri_Score = self.Vertical_score()
        hori_Score = self.Horizontal_score()
        diag_Score = self.Diagonal_score()
        
        if veri_Score == 100 or hori_Score == 100 or diag_Score == 100:
            return 100
        elif veri_Score == -100 or hori_Score == -100 or diag_Score == -100:
            return -100
        else:
            return veri_Score+hori_Score+diag_Score

    def Score_hard(self):
        self.score_Values = (0,5,20,100)
        
        veri_Score = self.Vertical_score()
        hori_Score = self.Horizontal_score()
        diag_Score = self.Diagonal_score()
        
        if veri_Score == 100 or hori_Score == 100 or diag_Score == 100:
            return 100
        elif veri_Score == -100 or hori_Score == -100 or diag_Score == -100:
            return -100
        else:
            return veri_Score+hori_Score+diag_Score

    #Create every possible board placement
    def Place_pieces(self):
        if self.depth%2 == 1:
            placing = self.opponent
        else:
            placing = self.player
        
        
        for the_Move in range(7):
            if self.board[0][the_Move] == " ":
                for i in range(0,6):
                    if self.board[i][the_Move] != " ": #If it falls and hits another piece.
                        new_Board = deepcopy(self.board)
                        new_Board[i-1] = new_Board[i-1][:the_Move] + placing + self.board[i-1][the_Move+1:]
                        self.possible_Moves.append((the_Move, new_Board))
                        break
                    elif i == 5:  #if it reaches the bottom of the Column.
                        new_Board = deepcopy(self.board)
                        new_Board[5] = new_Board[5][:the_Move] + placing + self.board[5][the_Move+1:]
                        self.possible_Moves.append((the_Move, new_Board))
                        break
                                




    #Get the vertical score of the current board
    def Vertical_score(self, scoring_Method = 0):
        negative_Score = 0
        positive_Score = 0
        
        for row in range(0,7):
            count = 0
            for col in range(0,6):
                if self.board[5-col][row] == self.player:
                    if count < 0:
                        count = 1;
                    else:
                        count += 1;
                elif self.board[5-col][row] == self.opponent:
                    if count > 0:
                        count = -1;
                    else:
                        count -= 1;
        
                # convert negative to positive for scoring index
                if count <= -4:
                    return -100
                elif count >= 4:
                    return 100
            if count < 0:
                negative_Score -= self.score_Values[abs(count)-1]
            elif count > 0:
                positive_Score += self.score_Values[count-1]
        return positive_Score + negative_Score
    

    #Get the horizontal score of the current board
    def Horizontal_score(self):
        negative_Score = 0
        positive_Score = 0
        
        for col in range(0,6):
            count = 0
            for row in range(0,7):
                if self.board[col][row] == self.player:
                    if count < 0:
                        count = 1;
                    else:
                        count += 1;
                elif self.board[col][row] == self.opponent:
                    if count > 0:
                        count = -1;
                    else:
                        count -= 1;
                if self.board[col][row] == " ":
                    count = 0
            
                if count <= -4:
                    return -100
                elif count >= 4:
                    return 100
            if count < 0:
                negative_Score -= self.score_Values[abs(count)-1]
            elif count > 0:
                positive_Score += self.score_Values[count-1]
        return positive_Score + negative_Score

    def Diagonal_score(self):
        negative_Score = 0
        positive_Score = 0
        
        for row in range(0,3):
            count = 0;
            for col in range(0,4):
                if self.board[col][row+col]==self.player:
                    if count < 0:
                        count = 1;
                    else:
                        count += 1;
                elif self.board[col][row+col]==self.opponent:
                    if count > 0:
                        count = -1;
                    else:
                        count -= 1;
                else:
                    count = 0;
                
                if count <= -4:
                    return -100
                if count >= 4:
                    return 100
            if count < 0:
                negative_Score -= self.score_Values[abs(count)-1]
            elif count > 0:
                positive_Score += self.score_Values[count-1]


        for row in range(3,6):
            count = 0;
            for col in range(0,5):
                if self.board[col][row-col]==self.player:
                    if count < 0:
                        count = 1;
                    else:
                        count += 1;
                elif self.board[col][row-col]==self.opponent:
                    if count > 0:
                        count = -1;
                    else:
                        count -= 1;
                else:
                    count = 0;
                
                if count <= -4:
                    return -100
                if count >= 4:
                    return 100
            if count < 0:
                negative_Score -= self.score_Values[abs(count)-1]
            elif count > 0:
                positive_Score += self.score_Values[count-1]
        return positive_Score - negative_Score