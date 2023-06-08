# -*- coding: utf-8 -*-
"""
Created on Thu May 26 08:39:39 2022

@author: Amy-Jay
"""
print("The game is ready")

#The function below checks if there are still available spaces to be played in.
def empty(list_):
    for item in list_:
        if "_" in item:
            return False
    else: 
        return True
    return False
#The function below checks if a player has won.
def iswon(subject, listt):
    
    #The function below caters for horizontal matching. 
    def func(rr, y, list__):
        if list__[0][y] == list__[1][y] == list__[2][y]== rr:
            return True
        else:
            return False
        
    #The function below caters for row or vertical matching.
    def func2 (aa, list_):
        for row in list_:
            if all(i == aa for i in row):
                return True
        return False
    
    #The function below caters for diagonal or cross-wise matching. 
    def diagonal(ss,lis):
        if lis[0][0] == lis[1][1] == lis[2][2] == ss:
            return True
        if lis[0][2] == lis[1][1] == lis[2][0] == ss:
            return True
    list_ = (0,1,2)
    
    #The following code merges all the functions such that any case where True, the player wins.
    if func2(subject, listt) == True or any(func(subject,x, listt) == True for x in list_ ) or diagonal(subject, listt):
        return True
    else:
        return False

#This is the main function for the progress of the game.
def playnow(xx):
    #The following code confirms a value, X or O for the computer.
    comp= "O"
    if xx== "O":
        comp ="X"
    ticlist= [["_","_","_"], ["_","_","_"], ["_","_","_"]]
    #This function prints the display of the game in an orderly arrangement.
    def print_():
        print("\n")
        for item in ticlist:
            print(*item)
    print_()
    #The loop below progresses the game, but breaks when 'empty' returns true or when any player wins.
    while True:
        #This variable is needed to break the outer while loop.
        det = 0
        x,y= [int(input("Row ")), int(input("Column "))]
        ticlist[(x-1)][y-1] = xx
        
        print_()
        if not iswon(xx, ticlist):
        
            import random
            import Connecto
            #The following loop helps the computer play only in a place that is empty for playing.
            while True:
                a = random.randint(1,3)
                b = random.randint(1,3)
                compchoose = ticlist[a-1][b-1]
                if compchoose == "_":
                   
                    brtlist = Connecto.intelligence(ticlist, xx)
                    if brtlist != 0:
                        r = brtlist[0]
                        s = brtlist[1]
                        if ticlist[r][s] == "_":
                            ticlist[r][s] = comp
                        else:
                            ticlist[a-1][b-1] = comp
                    else:
                        ticlist[a-1][b-1] = comp
                    
                    if iswon(comp, ticlist):
                        print_()
                        print("You Lose")
                        det = 1
                        input1 = input("Do you want to play again?/nYes or No? ")
                        if input1.lower() == "yes":
                            send()
                        else:
                            print("Thank you for playing this game.")
                    break
                else:
                    if empty(ticlist) == True:
                        print("Game Over")
                        input1 = input("Do you want to play again?/nYes or No? ")
                        if input1.lower() == "yes":
                            send()
                        else:
                           print("Thank you for playing this game.")
                        det = 1  
                    elif empty(ticlist) == False:
                        continue
                       
            if det == 1:
                break    
            print_()
        else:
            print("You Won!")
            input1 = input("Do you want to play again?/nYes or No? ")
            if input1.lower() == "yes":
                send()
            else:
                print("Thank you for playing this game.")
            break
        
#This is the initial function which collects user input and calls the inner functions.            
def play(x):
    if x== 0:
        print("Coward!")
    elif x== 1:
        print("Ready to play!")
        while True:
            try:
                XO= input("Are you X or O? ").lower()
                if XO != "x" and XO != "o":
                    raise ValueError
            except ValueError:
                continue
            else:
                playnow(XO.upper())
                break
    elif x=="2":
        print("Input yes or no")
        send()
dict_rez= {"yes":1,
           "no" : 0}



def send():
    input_= input("Are you ready to play? ").lower()
    value = dict_rez.get(input_,"2")
    play(value)

#The calling of the first operation starts here.
send()



            
            

    