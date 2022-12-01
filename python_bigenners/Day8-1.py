#Write your code below this line 👇
def prime_checker(number):
  for x in range(2,number):
    if number%x !=0:
      print("prime")
      break
    else:
      print("not")
      break
  

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


