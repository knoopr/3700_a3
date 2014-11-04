import os;
import sys;
import random;

PLAYERS = [ "Red", "Black" ];

NEXT_PLAYER = { PLAYERS[0]: PLAYERS[1], PLAYERS[1]: PLAYERS[0] };


class Board:
  def __init__( self, filename = None ):
    self.board = [];
    for col in range( 0, 7 ):
      self.board.append( [] );
      for row in range( 0, 6 ):
        self.board[col].append( " " );

    if not filename:
      self.move_no = 0;

      self.player = random.choice( PLAYERS );
      self.write();
    else:
      self.read( filename );

  def write( self ):
    fp = open( "board.%03d" % self.move_no, "w" );
    fp.write( str(self) );
    fp.close();

  def read( self, filename ):
    fp = open( filename );
    line = fp.readline();
    self.move_no = int( line.split(":")[-1].strip() );
    line = fp.readline();
    self.player = line.split("'")[0].strip();
    line = fp.readline(); # header line;
    for row in range(0,6):
      line = fp.readline();
      for col in range(0,7):
        self.board[col][row] = line[col];



  def __str__( self ):
    result = "Move: %d\n" % (self.move_no,);
    result += "%s's turn.\n" % (self.player);
    for col in range(0,7):
      result += "%d" % col;
    result += "\n";
    for row in range(0,6):
      for col in range(0,7):
        result += "%s" % self.board[col][row];
      result += "\n";
    return result;

  def turn( self ):
    os.system( "./%s board.%03d move.%03d"%(self.player,self.move_no,self.move_no) );
    fp = open( "move.%03d" % (self.move_no) );
    move = int( fp.readline() );
    fp.close();

    self.apply( move );

  def apply( self, move ):
    for row in range( 5, -1, -1 ):
      if self.board[ move ][ row ] == " ":
        self.board[ move ][ row ] = self.player[0];

        self.next_player();
        self.move_no += 1;
        self.write();
        return;
    raise Exception( "Bad move" );  # selected column is full, can't move there

  def next_player( self ):
    self.player = NEXT_PLAYER[ self.player ];

  def winner( self ):
    count = 0;
    for row in range(0,6):
      for col in range(0,7):
        if self.board[col][row]=="R":  # Red
          if count < 0:
            count = 1;
          else:
            count += 1;
        elif self.board[col][row]=="B":  # Black
          if count > 0:
            count = -1;
          else:
            count -= 1;
        else:
          count = 0;

        if count>=4:
          return "R";
        if count<=-4:
          return "B";

    count = 0;
    for col in range(0,7):
      for row in range(0,6):
        if self.board[col][row]=="R":  # Red
          if count < 0:
            count = 1;
          else:
            count += 1;
        elif self.board[col][row]=="B":  # Black
          if count > 0:
            count = -1;
          else:
            count -= 1;
        else:
          count = 0;

        if count>=4:
          return "R";
        if count<=-4:
          return "B";

    count = 0;
    for row in range(0,3):
      for col in range(0,4):
        if self.board[col][row+col]=="R":  # Red
          if count < 0:
            count = 1;
          else:
            count += 1;
        elif self.board[col][row+col]=="B":  # Black
          if count > 0:
            count = -1;
          else:
            count -= 1;
        else:
          count = 0;

        if count>=4:
          return "R";
        if count<=-4:
          return "B";

    count = 0;
    for row in range(3,6):
      for col in range(0,5):
        if self.board[col][row-col]=="R":  # Red
          if count < 0:
            count = 1;
          else:
            count += 1;
        elif self.board[col][row-col]=="B":  # Black
          if count > 0:
            count = -1;
          else:
            count -= 1;
        else:
          count = 0;

        if count>=4:
          return "R";
        if count<=-4:
          return "B";

    return None;

    
        
  def full( self ):
    """
    Return True if the board is full.
    """
    for col in range( 0, 7 ):
      for row in range( 0, 6 ):
        if self.board[col][row] == " ":
          return False;
    return True;

    
