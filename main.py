import random
number = random.randint(1, 10)

player = input('Hello! What is your name? ')
guesses_made = 0 
print('Welcome, {}! Let\'s play a game of "Guess The Number"! I will think of a number between 1 and 10 and you will take a guess, ok? Simply type in the number and press enter. Ready, set, GO!'.format(player))

correct = False

while correct == False:

  while True:
    try:
      guess = int(input('Your guess: '))
      if guess > 10:
        print('Perhaps I was unclear earlier, the number I\'m thinking of is between 1 and 10.')
        print('Don\'t worry, I won\'t count that as a round! Try again... ')
        continue
      else:
        break
    except ValueError:
      print('You have to guess a number, using digits. Try again!')
      continue


  guesses_made += 1
  if guess > number:
    print('That is a wee bit too high, maybe try to go down a little!')
  if guess < number:
    print('Try to go a little higher!')
  if guess == number:
    correct = True
    if guesses_made == 1: 
      print('You did it {0}! {1} was indeed the number I was thinking of! You guessed it straight away! Amazing! '.format(player, number))
    else:
      print('You did it {0}! {1} was indeed the number I was thinking of! It took you {2} tries in total to get there! Well done! '.format(player, number, guesses_made ))  
      