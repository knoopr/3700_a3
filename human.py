#!/usr/bin/python
import sys;

from Board import Board;

def main():
  board = Board( sys.argv[1] );
  print( "Your turn: %s\n" % (board.player,) );
  print( "%s\n" % board );
  
  print( "Select move 0-6:\n" );
  move = int( sys.stdin.readline() );

  fp = open( sys.argv[2], "w" );
  fp.write( "%d\n" % move );
  fp.close();

if __name__ == "__main__":
  main();
