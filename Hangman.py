# pip install random-word
#from random_word import RandomWords

from random import *
import getpass

#word = RandomWords()
#word.get_random_word()
#words = ['orange', 'apple', 'banana']
word = getpass.getpass("Input your word: ").lower()

print("answer: "+ word)
letters = ""
# r = RandomWords()
# r.get_random_words() : in list
# r.word_of_the_day() : Return Word of the day

count = 0

while True:
    print()
    success = True
    for w in word:
        if w in letters:
            print(w, end =" ")
        else:
            print("_", end = " ")
            success = False
    print()
    if success:
        print("success")
        break

    letter = input("Input letter > ").lower()

    if letter not in letters:
        letters += letter
    if letter in word:
        print("correct")
    else:
        print('wrong')
        count += 1
        if count == 5:
            print('game over')
            break
