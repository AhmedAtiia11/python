import random
import game_data
# import art

def choices():
  a=random.choice(game_data.data)
  b=random.choice(game_data.data)
  print(f"the name is {a['name']} ")
  print(f"the name is {b['name']} ")
  
  return a,b

def a_is_winner(a,b):
  if a['follower_count'] > b['follower_count']:
        return True
  else:
        print("you lose ..")
        return False   
        
          
def b_is_winner(a,b):          
  if b['follower_count'] > a['follower_count']:
    return True
  else:
    print("you lose ..")
    return False
      
print("Welcome to the guessing game ")
# print(art.logo)

def play():
  count=0
  while True:
    a,b=choices()
    while a['follower_count'] == b['follower_count']:
          a,b=choices()

    user=input("do you want to choose a or b: ")
    if user=='a':
      if a_is_winner(a,b) ==  True:
        count+=1
        # print(count)
      else :
        print(count)
        if input("Do you want to play again: ")=='y':
          play()
        else:
          break
        
    else:
      if b_is_winner(a,b)==True:
        count+=1
        # print(count)
      else :
        print(count)
        if input("Do you want to play again: ")=='y':
          play()
        else:
          break

play()        