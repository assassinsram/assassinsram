"""
It's a game that the player throw a dice. If he/she got any number but 1, it will
be added to his/her total score. But if he/she got number 1, his/her total score will
restart at zero and his/her round will finish. Now it's the other player turn.
If the player didn't want to throw the dice and save his/her total score, his/her 
turn will finish and the other player will start.
The game will finish when one of the two players has collected 25 or above
in his/her total score.
If the player entered a wrong input, the game will give a caution and it will continue.
"""

import random

total_1=0
total_2=0

while True:
    
    
    print("\n\nplayer 1 Turn")
    while True:
        action_1 = input("\nenter your action(roll,stop): ") #make the user decide his action.
        
        if action_1.lower() == "roll": #if the action was roll, it will generate an int num btwn 1&6.
            result_1 = random.randint(1, 6)
            print("rolling...",result_1)
            if result_1 != 1:       #if the result wasn't 1 it will be added to the total score.
                total_1 += result_1
                print("player one total score is:",total_1)
                if total_1 >= 25:     #if the total score is 25 or above you will win.
                    print("\ncongratulations player one win!!!!!!")
                    break
            else:      #if the result was 1 the total score will restart from zero and your turn finish.
                total_1 = 0
                print("player one total score is:",total_1)
                break
            
        elif action_1.lower() == "stop":  #if the action was stop, it will just print your total score.
            print("player one total score:",total_1)
            break
        
        else:           #if the user entered a wrong input it will give caution and restart the loop.
            print("you need to enter roll or stop.")
            continue



    if total_1>=25:
        break



    print("\n\nplayer 2 Turn")
    while True:
        action_2 = input("\nenter your action(roll,stop): ") #make the user decide his action.
        
        if action_2.lower() == "roll": #if the action was roll, it will generate an int num btwn 1&6.
            result_2 = random.randint(1, 6)
            print("rolling...",result_2)
            if result_2 != 1:       #if the result wasn't 1 it will be added to the total score.
                total_2 += result_2
                print("player two total score is:",total_2)
                if total_2 >= 25:     #if the total score is 25 or above you will win.
                    print("\ncongratulations player two win!!!!!!")
                    break
            else:      #if the result was 1 the total score will restart from zero and your turn finish.
                total_2 = 0
                print("player two total score is:",total_2)
                break
            
        elif action_2.lower() == "stop":  #if the action was stop, it will just print your total score.
            print("player two total score:",total_2)
            break
        
        else:           #if the user entered a wrong input it will give caution and restart the loop.
            print("you need to enter roll or stop.")
            continue
    
    
    if total_2>=25:
        break
