import random


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



word_list = ['Lion', 'Dolphin', 'Elephant', 'Giraffe', 'Penguin', 'Tiger', 'Koala', 'Eagle', 'Octopus', 'Cheetah']

word_pick = random.choice(word_list)

tries = 0
lives = 7
blank_list = []
counter = 0
print(word_pick)
end_of_game = False

for tback in range(0, len(word_pick)):
    blank_list.append("_")

while not end_of_game:
    guess = input('Guess a letter: ').lower()
    counter = 0
    for letter in word_pick.lower():
        if letter == guess:
            blank_list[counter] = guess
        counter += 1

    print(f"{' '.join(blank_list)}")

    if guess not in word_pick.lower():
        lives-=1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print('You Lose')


    if "_" not in blank_list:
        end_of_game = True
        print("You win!")
