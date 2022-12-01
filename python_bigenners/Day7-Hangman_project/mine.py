import random 
import hangman_art
import hangman_words
print(hangman_art.logo)


#Definitions
com_list=[]
word=[]
final=""
lives=7


com=random.choice(hangman_words.word_list)
for i in range(len(com)):
    com_list.append(com[i])


#for debugging --> 
print(com_list)

for i in range(len(com)):
    word.append("_")
print(word)

trails=len(com)+100  

while trails > 0 and lives >0:
  if word != com_list:
    user=input("Please enter you letter: ").lower()
    if user not in com_list:
        lives-=1
        print(hangman_art.stages[lives])
    if user in word:
        print("you have already choose that letter") 
        print(word)
        continue   
    for x in range(len(com)):
        if user==com_list[x]:
            word[x]=user
            print(word)

  trails-=1


for x in range(len(word)):
    final+=word[x]

if final==com:
    print(f"Congratulations, The final word is {final}")
else:
    print("you Died ,Piece of shit")
