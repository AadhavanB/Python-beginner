import time 
import random
i=0
j=0
win="Loser!"
lose="Winner!"
draw="Draw!"
print("Rock, Paper, Scissors, Shoot!")
while i<=10 or j<=10:
    lists=("Rock","Paper","Scissors")
    comp=random.choice(lists)
    hum=str(input("Enter your output:",))
    if hum=="Rock" and comp=="Paper":
        print("I say",comp)
        time.sleep(0.5)
        print("You chose",hum,"I win!")
        time.sleep(0.5)
        print(win)
        j+=1
        print("Your score:",i,"My score:",j)
    elif hum=="Scissors" and comp=="Rock":
        print("I say",comp)
        time.sleep(0.5)
        print("You chose",hum,"I win!")
        time.sleep(0.5)
        print(win)
        j=+1
        print("Your score:",i,"My score:",j)
    elif hum=="Paper" and comp=="Scissors":
        print("I say",comp)
        time.sleep(0.5)
        print("You chose",hum,"I win!")
        time.sleep(0.5)
        print(win)
        j+=1
        print("Your score:",i,"My score:",j)
    elif hum=="Paper" and comp=="Rock":
        print("I say",comp)
        time.sleep(0.5)
        print("You chose",hum,"I lose!")
        time.sleep(0.5)
        print(lose)
        i+=1
        print("Your score:",i,"My score:",j)
    elif hum=="Scissors" and comp=="Paper":
        print("I say",comp)
        time.sleep(0.5)
        print("You chose",hum,"I lose!")
        time.sleep(0.5)
        print(lose)
        i+=1
        print("Your score:",i,"My score:",j)
    elif hum==comp:
        print("I say",comp)
        time.sleep(0.5)
        print("awww, its a draw, so sad")
        time.sleep(0.5)
        print(draw)
        j+=1
        i+=1
        print("Your score:",i,"My score:",j)
    elif hum=="Rock" and comp=="scissors":
        print("I say",comp)
        time.sleep(0.5)
        print("You chose",hum,"I lose!")
        time.sleep(0.5)
        print(lose)
        i+=1
        print("Your score:",i,"My score:",j)
    if i==10 or j==10:
        print("Games over bye!")
        break
print("A game by XXɅ) 2∅24")
