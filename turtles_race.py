from turtle import Turtle,Screen
import random
screen=Screen()      
screen.setup(width=650,height=400)

def play():
    colors=["red","blue","purple","orange","green","brown","black"]
    turtles=[]
    game_is_on=False
    winning=""
    y_positions=[-150,-100,-50,0,50,100,150]


    for i in range (7):
        tim=Turtle(shape="turtle")
        tim.color(colors[i])
        tim.penup()
        tim.goto(-325,y_positions[i])
        turtles.append(tim)


    user_bet=screen.textinput("Bet", "Choose the color of turtle you bet on").lower()
    if user_bet:
        game_is_on=True

    while game_is_on: 
        for turtle in turtles:
            turtle.forward(random.randint(0,10))
            if turtle.xcor()>300.0:
                winning=turtle
                game_is_on=False

    if user_bet:   
        print(f"the winning turtle is {winning.pencolor()} and your bet is {user_bet}")
        if winning.pencolor()==user_bet:
            print("You are the winner")
        else:
            print("You lose")
        
    play_again=input("Do you want to play again: ")
    if play_again=="yes":
        screen.clear() 
        play()
    else:
        screen.bye()
        return 0
play()
# screen.exitonclick()   
