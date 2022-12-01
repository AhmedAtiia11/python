import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("Enter 0 for Rock \nEnter 1 for Paper \nEnter 2 for Scissors\n")
user=input("Enter your choice: ")
if user == "0":
  print (rock)
elif user == "1":
  print(paper)
else :
  print(scissors)
  
com=str(random.randint(0,2))
print(f"computer choice is {com}")
if com == "0":
  print (rock)
elif com == "1":
  print(paper)
else :
  print(scissors)
if (user=="0" and com == "0")or(user=="1" and com =="1")or(user=="2" and com =="2"):
   print ("Draw")
elif (user =='0' and com == "1") or (user=="1" and com =="2") or (user=="2" and com == "0"):
   print("you lose piece of shit")
elif (user =="0" and com =="2") or (user=="1" and com =="0") or (user=="2" and com =="1"):
  print("Lucky shot")
  