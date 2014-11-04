import os;
import random;
from sys import argv;
from Board import Board;

def main():
  board = Board();

  try:
    while not board.winner() and not board.full():
      board.turn();

    print( "Winner: ", board.winner() );
    print( "Game over!" );
  except Exception as e:
    print( "Player", board.player, "has been disqualified!" );
    board.next_player();
    print( "Winner: ", board.player );
    print( "Game over!")

if __name__ == "__main__":
  main();
  if len(argv) == 2 and argv[1] == "1":
    os.system("find ./ -type f | grep '\.[0-9]' | xargs /bin/rm ")
