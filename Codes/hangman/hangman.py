# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
	def __init__(self, word):
		global letters
		global fill
		self.remaining_guesses = 9
		self.status = STATUS_ONGOING
		letters = list(word)
		blanks = len(letters)
		fill = ['_' for i in range(blanks)]
		print(' '.join(fill))
		
	
	def guess(self, char):
		global letters
		if char in letters:
			index = [j for j, value in enumerate(letters) if value == char]
#			letters = [i for i in letters if i != char]
			global fill
			for insert in index:
				fill[insert] = char
#			print(type(fill))
#			fill = list(filter(lambda x, y: y if y != '_' else char if x in index else '_', enumerate(fill))) 
#			print(type(fill))

		else:
			self.remaining_guesses = self.remaining_guesses - 1
			if self.remaining_guesses == 0:
				return STATUS_LOSE

	def get_masked_word(self):
		s = ''
		s = s.join(letters)
		return s

	def get_status(self):
		global fill
		print(' '.join(fill))
		if not '_' in fill:
			return STATUS_WIN
		elif '_' in fill and self.remaining_guesses == 0:
			return STATUS_LOSE
		else:
			return STATUS_ONGOING


game = Hangman("FOOD")
while(game.get_status() == STATUS_ONGOING):
	game.guess(input('Guess a letter'))
	print(game.get_status())
print(game.get_status())
