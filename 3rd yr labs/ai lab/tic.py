class TTTBoard:
	def __init__(self):
		"""Initialize a 3x3 tic tac toe board. The board should contain a single attribute, a list, that initially contains nine star characters.  This list contains contents of the board.  A star denotes that this position has not yet been claimed by 'X' or 'O'.  Again, this is simply a flat list of 9 items, not a list of lists."""
		self.board = ['*','*','*','*','*','*','*','*','*']
		self.count = 0  #used for tracking the number of moves that have been made.  If == 8, then game cannot continue.

	def __str__(self):
		"""Returns a string representation of the board. Instead of just displaying a flat list of the 9 items, I want you to display this list like a tic tac toe board, with 3 rows of 3 items each. See the test file output for what this looks like."""
		return str(self.board[0])+"|"+str(self.board[1])+"|"+str(self.board[2])+"\r\n"+"--"+"--"+"--"+"\r\n"+str(self.board[3])+"|"+str(self.board[4])+"|"+str(self.board[5])+"\r\n"+"--"+"--"+"--"+"\r\n"+str(self.board[6])+"|"+str(self.board[7])+"|"+str(self.board[8])
	
	def makeMove(self,player,pos):
		"""Places a move for player in the position pos (where the board squares a numbered from left to right, starting in the top left squares with 0, and beginning at the left in each new row), if possible.  'player' is a character ('X' or 'O') and pos is an integer.  Returns True if the move was made and False if not (because te spot was full, or outside the boundaries of the board)."""
		if self.board[pos] == "*":  # checks to see if a move has been made already
			self.board[pos] = player
			self.count += 1
			return True
		else:
			return False
	
	def hasWon(self,player):
		"""Returns True if player has won the game, and False if not"""

		# check diagonals
		if self.board[0] == player and self.board[4] == player and self.board[8] == player:
			return True
		elif self.board[2] == player and self.board[4] == player and self.board[6] == player:
			return True

		# check horizontals
		elif self.board[0] == player and self.board[1] == player and self.board[2] == player:
			return True
		elif self.board[3] == player and self.board[4] == player and self.board[5] == player:
			return True
		elif self.board[6] == player and self.board[7] == player and self.board[8] == player:
			return True

		# check verticals
		elif self.board[0] == player and self.board[3] == player and self.board[6] == player:
			return True
		elif self.board[1] == player and self.board[4] == player and self.board[7] == player:
			return True
		elif self.board[2] == player and self.board[5] == player and self.board[8] == player:
			return True

		# if nothing, return false
		return False

	def gameOver(self):
		"""Returns True if someone has won or if the board is full, False otherwise"""
		if self.hasWon('X') :
			return 'X'
		elif self.hasWon('O'):
			return 'O'
		
		elif self.count>=8:
			return 'D'
		
		else:
			return 'F'

	def clear(self):
		"""Clears the board to reset the game"""
		self.board = ['*','*','*','*','*','*','*','*','*']
		self.count = 0

if __name__ == "__main__":
	print("player1=>X and player2 =>O\n game starts now.....")
	t=TTTBoard();
	count=0
	while(1):
		print("\n")
		print(t.__str__())
		print("\n")
		
		print("player %d turn => select ur position\n" %((count%2) +1))
		
		pos = input("")
		pos=pos-1;
		if count == 0:
			t.makeMove('X', pos)
		else:
			t.makeMove('O', pos) 
		
		if t.gameOver() != 'F':
			print("\n")
			print(t.__str__())
			print("\n")
		
			if t.gameOver() == 'O':
				print('\nplayer 2 won')
			elif t.gameOver() == 'X':
				print('\nplayer 1 won')
			elif t.gameOver() == 'D':
				print('\ngame draw')
			break				


		count+=1;
		count=count%2
		

# 0 1 2
# 3 4 5
# 6 7 8





