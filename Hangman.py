# pip install random-word

from random_word import RandomWords
from random import *

words = RandomWords()
word = words.get_random_word()
# r = RandomWords()
# r.get_random_words() : in list
# r.word_of_the_day() : Return Word of the day
print("answer: "+ word)
letters = ""

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

    letter = input("Input letter > ")
    if letter not in letters:
        letters += letter
    if letter in word:
        print("correct")
    else:
        print('wrong')
