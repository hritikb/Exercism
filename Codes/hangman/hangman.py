# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
	letters=[]
	def __init__(self, word):
		global letters
		self.remaining_guesses = 9
		self.status = STATUS_ONGOING
		letters = list(word)
		

	def guess(self, char):
		global letters
		if char in letters:
			letters = [i for i in letters if i != char]
			print(letters)

		else:
			self.remaining_guesses = self.remaining_guesses - 1
			if self.remaining_guesses == 0:
				return STATUS_LOSE

	def get_masked_word(self):
		s = ''
		s = s.join(letters)
		return s

	def get_status(self):
		if len(letters) == 0:
			return STATUS_WIN
		elif len(letters) != 0 and self.remaining_guesses == 0:
			return STATUS_LOSE
		else:
			return STATUS_ONGOING, self.remaining_guesses


game = Hangman("SHERLOCK")
game.guess(input('Guess a letter'))
print(game.get_status())
game.guess(input('Guess a letter'))
print(game.get_status())
game.guess(input('Guess a letter'))
print(game.get_status())
game.guess(input('Guess a letter'))
print(game.get_status())
game.guess(input('Guess a letter'))
print(game.get_status())
game.guess(input('Guess a letter'))
print(game.get_status())
game.guess(input('Guess a letter'))
print(game.get_status())
game.guess(input('Guess a letter'))
print(game.get_status())
game.guess(input('Guess a letter'))
print(game.get_status())