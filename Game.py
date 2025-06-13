'''
num code:
stone = 0
paper = 1
scissor = 2
'''
import random
import time
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate',145)
engine.setProperty('volume',1.0)
engine.say("Welcome to the Game zone")
engine.runAndWait()
startup = print("GAME 🎮 \n STONE 🌑, PAPER 📜, SCISSOR ✂️"),time.sleep(2)
engine.say("Lets get started")
engine.runAndWait()
print("Lets get started 🏁"),time.sleep(1.3)

for i in range(5):
    engine.say(f"Round {i + 1}")
    print(f"\n🔁 Round {i + 1}"),time.sleep(1)
    engine.runAndWait()
    computer = random.randint(0,2)
    youchoose = input("Enter your choice: ").lower()
    youdict = {"stone": 0, "paper": 1, "scissor": 2}
    try:
        you = youdict[youchoose]
    except KeyError:
        print("❌ Invalid input. Please type: stone, paper, or scissor.")
    continue

    def main():
        if (computer == 0) and (you == 1):

            print(f"🤖 Juno chose: Stone 🌑 \n")
            print("You Win 🏆\n Juno lose")
         
        elif (computer == 0) and (you == 2):
            print(f"🤖 Juno chose: Stone 🌑 \n")
            print("You lose ❌\n Juno win")
        elif (computer == 0) and(you == 0): 
            print(f"🤖 Juno chose: Stone 🌑 \n")
            print("Game Draw")

        elif (computer == 1) and (you == 2):
            print(f"🤖 Juno chose: Paper 📜 \n")
            print("You Win 🏆\n Juno lose")
        elif (computer == 1) and (you == 0):
            print(f"🤖 Juno chose: Paper 📜 \n")
            print("You lose ❌\n Juno win")
        elif (computer == 1) and(you == 1): 
            print(f"🤖 Juno chose: Paper 📜 \n")
            print("Game Draw")


        elif (computer == 2) and (you == 0):
            print(f"🤖 Juno chose: Scissor ✂️ \n")
            print("You Win 🏆\n Juno lose")
        elif (computer == 2) and (you == 1):
            print(f"🤖 Juno chose: Scissor ✂️ \n")
            print("You lose ❌\n Juno win")
        elif (computer == 2) and(you == 2): 
            print(f"🤖 Juno chose: Scissor ✂️ \n")
            print("Game Draw")
        elif youchoose != youdict:
            print("Your choice is invalid")
        
    main()
print("\n🎮 Game Over! Thanks for playing.")
print("\n Wanna try again 🔁 ")





