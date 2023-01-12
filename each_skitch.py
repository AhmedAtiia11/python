from turtle import Turtle,Screen
tim=Turtle()
tim.shape("turtle")
screen=Screen()
def forward():
    tim.forward(10)
def backward():
    tim.backward(10)
def clock_wise():
    tim.setheading(tim.heading()-10)
def counter_clock_wise():
    tim.setheading(tim.heading()+10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()   
    tim.pendown()
 
screen.listen()
screen.onkey(key="w",fun=forward)    
screen.onkey(key="s",fun=backward)    
screen.onkey(key="d",fun=clock_wise)    
screen.onkey(key="a",fun=counter_clock_wise)   
screen.onkey(key="c",fun=clear)    

screen.exitonclick()