# from art import logo
# print(logo)

def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def mul(n1,n2):
  return n1*n2
def dev(n1,n2):
  return n1/n2  

  
def choice(num1,num2,operation):
  sum=0
  if operation == "+":
    sum+=add(num1,num2)
  elif  operation == "-":
    sum+=sub(num1,num2) 
  elif operation == "*":
    sum+=mul(num1,num2)
  elif operation == "/":
    sum+=dev(num1,num2)  
  return sum

def calculator():
  total_sum=0
  y=True
  
  num1=int(input("Enter your first number: "))
  operation=input("Enter your op:\n+\n-\n*\n/\n==> ")
  num2=int(input("Enter your second number: "))
  total_sum+=choice(num1,num2,operation)
  while y:
    print(total_sum)
    z=input(f"your sum is {total_sum} do you want to continue: ")
    if z == "yes":
      num1=int(input("enter your num: "))
      operation=input("enter your op: ")
      total_sum=choice(num1,total_sum,operation)
    else:
      calculator()
    

calculator()