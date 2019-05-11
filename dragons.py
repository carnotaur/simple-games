import random 
import time

def displayIntro():
	print('''2 пещеры - 2 дракона - все или ничего. 
В одной пещеры щедрый дракон - богаства, малибу, яхты, пинаколода и всем тому подобное
В другом судьба быть переваренным к завтрашнему обеду...''', end='\n\n')

def chooseCave():
	cave = ''
	while cave not in ['1', '2']:
		print('В какую пещеру вы войдете? В 1 или 2?')
		cave = input()

	return cave

def checkCave(chosenCave):
	print('Вы приближаетесь к пещере...')
	time.sleep(2)
	print('Ее темнота заставляет вас дрожать от страха..')
	time.sleep(2)
	print('Большой дракон выпрыгивает перед вами и...', end='\n\n')
	time.sleep(2)


	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('...делится с вами своими сокровищами')
	else:
		print('...сьедает вашу башку!!!')


if __name__ == '__main__':

	playAgain = 'да'

	while playAgain in ['да', 'д']:
		displayIntro()
		caveNumber = chooseCave()
		checkCave(caveNumber)

		print('Попытает удачу еще раз? Да или нет')
		playAgain = input().lower()
