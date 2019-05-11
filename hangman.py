import random
import time
import string


with open('words.txt', mode='r') as file:
    WORD_LIST = list(map(lambda word: word.strip(), file.readlines()))
    WORD_LIST = [word for word in WORD_LIST if len(word) < 6 and len(word) > 3]


HAGMANS = ('''
 +--+
 |  |
    |
    |
    |
   ---''', '''
 +--+
 |  |
 0  |
    |
    |
   ---''', '''
 +--+
 |  |
 0  |
 |  |
    |
   ---''', '''
 +--+
 |  |
 0  |
 |\ |
    |
   ---''', '''
 +--+
 |  |
 0  |
/|\ |
    |
   ---''', '''
 +--+
 |  |
 0  |
/|\ |
  \ |
   ---''', """
 +--+
 |  |
 0  |
/|\ |
/ \ |
   ---
"""
)

def calculate_correct_part(correct_letters, secret_word):
	blank = '_' * len(secret_word)
	correct_part = [
	secret_word[idx] 
	if secret_word[idx] in correct_letters
	else blank_letter
	for idx, blank_letter in enumerate(blank) 
	]
	return correct_part, blank


def makeBoard(correct_letters, incorrect_letters, secret_word):
	correct_part, blank = calculate_correct_part(correct_letters, secret_word)
	print('Hangamn READY TO DIE YEAHH??:')
	print(HAGMANS[len(incorrect_letters)])
	print('Correct part there: oooo_OOOO')
	print(''.join(correct_part), end='\n\n')
	print('YOUR Errors DUMB:')
	print('-'.join(incorrect_letters))
	return correct_part
	
def takeInput(incorrect_letters, correct_letters):
	print('Guess letter in word:')
	letter = input().lower()

	if len(letter) > 1:
		print('Write LETTER')
		takeInput(incorrect_letters, correct_letters)

	if letter not in string.ascii_lowercase:
		print('Letter should be Latin!')
		takeInput(incorrect_letters, correct_letters)

	if letter in incorrect_letters + correct_letters:
		print(' Letter was already guessed O_O, TRY BETTER')
		takeInput(incorrect_letters, correct_letters)

	print('---- Your GUESSS IS THIS: %s' % letter, end='\n\n')
	return letter

def startGame():
	correct_letters = []
	incorrect_letters = []
	secret_word = random.choice(WORD_LIST)
	print(' ohh lets see who are there? ')
	print(' Some poor bastard ready to be hanged. Can YOU save him?')
	print('Guess word that I chosen and hangman will be saved, otherwise HE WILL DIE')
	time.sleep(2)

	while True:
		correct_part = makeBoard(correct_letters, incorrect_letters, secret_word)

		if ''.join(correct_part) == secret_word:
			print("WOOOOW HAHAHHAHA It\'s Surprise")
			print('YOU WON!!! WINNER')
			print(secret_word)
			break

		letter = takeInput(correct_letters, incorrect_letters)

		time.sleep(2)
		if letter in secret_word:
			print('--- Wow we have some brains there! You\'re right!')
			correct_letters.append(letter)
		else:
			print('--- BAD BAD BAD -- Try better, little FOOL!')
			incorrect_letters.append(letter)

		if len(incorrect_letters) >= len(HAGMANS) - 1:
			print('ohhh he died')
			print('YOU LOSE!!! LOSER!!!')
			print(secret_word)
			break

		time.sleep(2)
		print('!!!!Let\'s CONTINUE SHOW!!!!!!', end='\n\n')
		print('-' * 30)
		time.sleep(1)




if __name__ == '__main__':
	breakGame = False
	while breakGame is False:
		startGame()
		print('Want another try little girl? YES OR NO')
		answer = input()
		if answer.lower() == 'yes':
			breakGame = False
		else:
			breakGame = True
	