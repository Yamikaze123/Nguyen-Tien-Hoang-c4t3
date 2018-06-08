import random
print("Welcome to word jumble")
print("Demo with 3 words")
word = int(input("You want word number?"))

wordlist = ["foot","change","computer"]
word1 = ["f","o",'o',"t"]
word2 = ["c","h","a","n","g","e"]
word3 = ["c","o","m","p","u","t","e","r"]

if word == 1:
    random.shuffle(word1)
    print(word1)
    answer1 = input("Your answer?")
    if answer1 == "foot":
        print("Hura")
    else:
        print("Sad")
elif word == 2:
    random.shuffle(word2)
    print(word2)
    answer2 = input("Your answer?")
    if answer2 == "change":
        print("Hura")
    else:
        print("Sad")
elif word == 3:
    random.shuffle(word3)
    print(word3)
    answer3 = input("Your answer?")
    if answer3 == "computer":
        print("Hure")
    else:
        print("Sad")


