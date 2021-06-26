# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
	def __init__(self, word):
		self.remaining_guesses = 9
		self.status = STATUS_ONGOING
		self.letters = list(word)
		self.blanks = len(self.letters)
		self.fill = ['_' for i in range(self.blanks)]
		self.guessed = []
		
	
	def guess(self, char):
		if self.status != STATUS_ONGOING:
			raise ValueError('.+')
		if char in self.letters and char not in self.guessed:

			index = [j for j, value in enumerate(self.letters) if value == char]
			
			for insert in index:
				self.fill[insert] = char
			
			if not '_' in self.fill:
				self.status = STATUS_WIN 
			
			

		else:
			self.remaining_guesses = self.remaining_guesses - 1
			if self.remaining_guesses < 0:
				self.status = STATUS_LOSE

		self.guessed.append(char)

	def get_masked_word(self):

		return ''.join(self.fill)

	def get_status(self):
		return self.status







