# Name: Jamar Hill
# Date: 12/2/2020
# Description: Assignment 10

class BuildersGame:
    def __init__(self):
        #Establish board on a 5x5 grid of lists, each list contains five empty strings.
        self.board =[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self.current_state = "UNFINISHED" #To correspond with get_current_state
        self.turn = 'x'
        self.xmv1 = None
        self.xmv2 = None
        self.omv1 = None
        self.omv2 = None

# Get method which returns current state
    def get_current_state(self):
        return  self.current_state
    #(x1,y1) represent first move. (x2,y2) represent second move
    def _is_adjacent(self,x1,y1,x2,y2):

        #Adding 1 and subtracting 1 to the x and y coordinates on the grid allows us to determine if moves are adjacent
        if (x1==x2 and y1+1==y2) or(x1==x2 and y1-1==y2) or (x1+1 == x2 and y1-1 == y2) or(x1+1==x2 and y2==y1) or (x1+1==x2 and y1+1==y2)\
                or (x1-1==x2 and y1-1==y2) or (x1-1==x2 and y1==y2) or (x1-1==x2 and y1+1==y2) :

             return True #If true, the move is considered to be adjacent

        else:

            return False #If false, the move is not considered to be adjacent

    def initial_placement(self,x1,y1,x2,y2,player):
        if player == 'x' and self.turn!='o':
            self.turn = 'o'
            self.xmv1 = str(x1) + str(y1)
            self.xmv2 = str(x2) + str(y2)
            #self.xmv1 and self.xmv2 will add elements of the move to the string

        elif player == 'o' and self.turn!='x':
            self.turn='x'
            vars_of_mv1 = str(x1) + str(y1)
            vars_of_mv2 = str(x2) + str(y2)
            # vars.xmv1 and vars.xmv2 will add elements of the move to the string

            #By checking to see if the elements of self.xmv1, self.mv2, vars.mv1, and vars.mv2 are equal we can determine if the square is occupied
            if self.xmv1 != vars_of_mv1 and self.xmv1!=vars_of_mv2 and self.xmv2!=vars_of_mv1 and self.xmv2!=vars_of_mv2:
                self.omv1 = vars_of_mv1
                self.omv2 = vars_of_mv2

            else:
                print("Square Occupied")
                return  False

        else:
            print("Invalid")
            return False

    def make_move(self,x1,y1,x2,y2,x3,y3):
        pos_of_bldr = str(x1) + str(y1)
        pos_of_dest = str(x2)+str(y2)

        if self.turn == 'x':
            self.turn = 'o'

            if self.omv1!=pos_of_bldr and self.omv2!=pos_of_bldr:

                if self.omv1!=pos_of_dest and self.omv2!=pos_of_dest and self.xmv1!=pos_of_dest and self.xmv1!=pos_of_dest:


                    if self.board[x2][y2] - self.board[x1][y1]<2:

                        if self._is_adjacent(x2,y2,x3,y3):
                            if self.xmv1 == pos_of_bldr:
                                self.xmv1 = pos_of_dest
                            else:
                                self.xmv2 = pos_of_dest

                            #Establishng Player x as the Winner
                            if self.board[x2][y2]==3:
                                self.current_state = 'X_WON'
                                return True

                            #Player Move Up By One
                            if self.board[x2][y2]!=3 and self.board[x2][y2]!=4:
                                self.board[x2][y2]+=1

                            #Establishes Player o as the Winner
                            if self.board[x2][y2]!=3 and self.board[x2][y2]==4:
                                self.current_state = 'O_WON'
                                return  True

                        else:
                            print('Error: Not Adjacent Move')
                            self.turn='x'
                            return  False
                    else:
                        print('Error: Move Requires Height Greater Than 1')
                        self.turn = 'x'
                        return False

                else:
                    print("Error: Square Is Currently Occupied")
                    self.turn = 'x'
                    return  False
            else:
                print("Error: Incorrect Builder")
                self.turn = 'x'
                return  False

        elif self.turn == 'o':
            self.turn = 'x'

            #Condition for picking out of turn
            if self.xmv1 != pos_of_bldr and self.xmv2 != pos_of_bldr:

                #Condition for the square not being occupied
                if self.omv1 != pos_of_dest and self.omv2 != pos_of_dest and self.xmv1 != pos_of_dest and self.xmv1 != pos_of_dest:


                    if self.board[x2][y2] - self.board[x1][y1] < 2:

                        #Add level to square adjacent to move
                        if self._is_adjacent(x2, y2, x3, y3):

                            #Move
                            if self.omv1 == pos_of_bldr:
                                self.omv1 = pos_of_dest
                            else:
                                self.omv2 = pos_of_dest

                            #Player O wins
                            if self.board[x2][y2] == 3:
                                self.current_state = 'O_WON'
                                return True

                            #Out of Moves
                            if self.board[x2][y2] != 3 and self.board[x2][y2] != 4:
                                self.board[x2][y2] += 1

                            #Player X Wins
                            if self.board[x2][y2] != 3 and self.board[x2][y2] == 4:
                                self.current_state = 'X_WON'
                                return True

                        else:
                            print('Error: None Adjacent Move')
                            self.turn = 'o'
                            return False

                    #Player attempts to move illegally
                    else:
                        print('Error: Move Requires Height Greater Than 1')
                        self.turn = 'o'
                        return False

                #Square is occupied
                else:
                    print("Error: Square Is Currently Occupied")
                    self.turn = 'o'
                    return False
            else:
                print("Error: Incorrect Builder")
                self.turn = 'o'
                return False

        else:
            print("Error: Player Move Is Out of Turn")
            return False


#Test
game = BuildersGame()
game.initial_placement(2,2,1,2,'x')
game.initial_placement(0,1,4,2,'o')
game.make_move(2,2,1,1,1,0)
game.make_move(0,1,1,0,2,0)
game.get_current_state()
print(BuildersGame())