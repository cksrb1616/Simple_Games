from random import *
words = ["apple", "banana", "orange"]
word = choice(words)
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
