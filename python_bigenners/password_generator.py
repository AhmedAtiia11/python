#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))

nr_numbers = int(input(f"How many numbers would you like?\n"))
password=""
for x in range(0,nr_letters):
  ran=random.randint(0,len(letters)-1)
  password=password+letters[ran]


for x in range(0,nr_symbols):
  ran=random.choice(symbols)
  password+=ran

for x in range(0,nr_numbers):
  ran=random.choice(numbers)
  password+=ran  

weak_pass=password



hard_password=""
for x in range(0,len(password)):
  num=random.randint(0,len(password)-1)
  hard_password=hard_password+password[num]



harder=[]
for x in range(0,len(weak_pass)-1):
    harder.append(weak_pass[x])

# print(harder)
random.shuffle(harder)


harder_pass=""
for x in range(0,len(weak_pass)-1):
    harder_pass+=harder[x]

print(f"this is weak pass in string format : {weak_pass}")
print(f"this is hard pass in string format : {hard_password}")
print(f"this is harder pass in list format: {harder}")
print(f"this is same harder pass in string format: {harder_pass}")    


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P