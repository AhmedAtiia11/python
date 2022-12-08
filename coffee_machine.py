#espresso latte cappuccino
MENU = { 
    "e": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "l": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "c": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def remain(order,remaining):
  remaining["water"]=remaining["water"]-MENU[order]["ingredients"]["water"]
  if order != "e":
    remaining["milk"]=remaining["milk"]-MENU[order]["ingredients"]["milk"]
  remaining["coffee"]=remaining["coffee"]-MENU[order]["ingredients"]["coffee"]
  return remaining


  
def check(remaining):
  flag=1
  for i in remaining:
    if remaining[i] < 0:
      print(f"There is no sufficient {i}")
      flag=0
  return flag


  
def money_change(cost):
  flag=1
  print("Please insert coins")
  quarters=int(input("How many quarters? "))
  dime=int(input("How many dimes? "))
  nickel=int(input("How many nickel? "))
  penny=int(input("How many penny? "))
  total=penny*.01+nickel*.05+dime*.1+quarters*.25
  if cost>total:
    print("Not enough money")
    flag=0
  return flag,total-cost  
  
remaining=resources
change=0
save=0
cont=True


while cont:
  order=input("What would you like to order? (Espresso,Latte,Cappuccino,Report) ").lower()
  
  if order =="r":
    print(f"The remaining ingredents are {remaining} and the saved money is {save}")
    
  elif order=="l" or order=="e" or order =="c":  
    cost=MENU[order]["cost"]
    flag,change=money_change(cost)
    if flag==1:
      remaining=remain(order,remaining)
      if check(remaining) !=0 :
        print(remaining)
    if change>=0:
      print(f"Here is the change:{change}")
      save+=MENU[order]["cost"]
      change=0    
    # save+=MENU[order]["cost"]
  
  else:
    print("Please choose from the above options ")
    continue

  if change>0:
    save+=change
    change=0
  y=input("want to continue(y/n): ")
  if y == "n":
    cont=False