import random

no = 5
print("Welcome to the game of Hangman!")
print("You have", no, "chances.")
print("All caps only!!!!!!!")

lis = ["TEA", "JOKER", "PASTA", "INDIA"]
for word in lis:
    i = 0
    print("The word has", len(word), "letters")

    while i < no:
        if word == "TEA":
            print("This particular word is familiar in parts of the North. Many people in the world mis-speak this word.")
            print("_ E _")

            let1 = str(input("The first letter: "))
            if let1 == "T":
                print("You are correct!")
            else:
                print("You are wrong")
                i += 1
                print("You have", no - i, "chances left.")
                continue

            let2 = str(input("The third letter: "))
            if let2 == "A":
                print("You are correct!")
                print("You win the game!")
                break
            else:
                print("You are wrong")
                i += 1
                print("You have", no - i, "chances left.")
                continue

        elif word == "JOKER":
            print("A movie has been made by DC with the name of this word.")
            print("J _ _ E _")

            let1 = str(input("The second letter: "))
            if let1 == "O":
                print("You are correct!")
            else:
                print("You are wrong")
                i += 1
                print("You have", no - i, "chances left.")
                continue
            let2 = str(input("The third letter: "))
            if let2 == "K":
                print("You are correct!")
            else:
                print("You are wrong")
                i += 1
                print("You have", no - i, "chances left.")
                continue
            let3 = str(input("The fifth letter: "))
            if let3 == "R":
                print("You are correct!")
                print("You win the game!")
                break
            else:
                print("You are wrong")
                i += 1
                print("You have", no - i, "chances left.")
                continue

        elif word == "PASTA":
            print("An Italian dish which is a delicacy in New York for the rich.")
            print("P _ _ _ A")
            let1 = str(input("The second letter: "))
            if let1 == "A":
                print("You are correct!")
            else:
                print("You are wrong")
                i += 1
                print("You have", no - i, "chances left.")
                continue

            let2 = str(input("The third letter: "))
            if let2 == "S":
                print("You are correct!")
            else:
                print("You are wrong")
                i += 1
                print("You have", no - i, "chances left.")
                continue
            let3 = str(input("The third letter: "))
            if let3 == "T":
                print("You are correct!")
                print("You win the game!")
                break
            else:
                print("You are wrong")
                i += 1
                print("You have", no - i, "chances left.")
                continue

        elif word == "INDIA":
            print("A country that had been colonised by the British and the East India Company")
            print("I _ D I A")

            let1 = str(input("The second letter: "))
            if let1 == "N":
                print("You are correct!")
                print("You win the game!")
                break
            else:
                print("You are wrong")
                i += 1
                print("You have", no - i, "chances left.")
                continue
    else:
        print("You have used all your chances. The word was:", word)
        break
    break

print("A game by XXɅ) 2∅24")
