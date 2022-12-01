# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 

# Then check for the number of times the letters in the word LOVE occurs. 

# Then combine these numbers to make a 2 digit number.
# e.g.

# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times

# R occurs 1 time

# U occurs 2 times

# E occurs 2 times

# Total = 5

# L occurs 1 time

# O occurs 0 times

# V occurs 0 times

# E occurs 2 times

# Total = 3

# Love Score = 53

# Print: "Your score is 53."
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1=name1.lower()
name2=name2.lower()
sum11=0
sum22=0
t=name1.count("t")+name2.count("t")
sum11 =t+sum11
r=name1.count("r")+name2.count("r")
sum11 +=r
u=name1.count("u")+name2.count("u")
sum11 +=u
e=name1.count("e")+name2.count("e")
sum11 +=e

l=name1.count("l")+name2.count("l")
sum22 +=l
o=name1.count("o")+name2.count("o")
sum22 +=o
v=name1.count("v")+name2.count("v")
sum22 +=v  
x=name1.count("e")+name2.count("e")
sum22 +=x  
score=str(sum11)+str(sum22)
if int(score) <10 or int(score)>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score)>40 and int(score)<50:
    print(f"Your score is {score}, you are alright together.") 
else:
    print(f"Your score is {score}.")       