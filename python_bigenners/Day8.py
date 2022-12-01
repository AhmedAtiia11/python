alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# #encryption function
# def encrypt(word_plain=text,shift=shift):
#   encrypted_word=""
#   for i in word_plain:
#     new_letter_index=alphabet.index(i)+shift
#     if new_letter_index > 25:
#       new_letter_index-=26
#     encrypted_word+=alphabet[new_letter_index]
#   print(f"this is the encrypted word : {encrypted_word}") 

# #decryption function
# def decrypt(word_plain=text,shift=shift):
#   decrypt_word=""
#   for i in word_plain:
#     new_letter_index=alphabet.index(i)-shift
#     if new_letter_index < 0:
#       new_letter_index+=26
#     decrypt_word+=alphabet[new_letter_index]
#   print(f"this is the decrypted word : {decrypt_word}") 


# if direction == "encode" :
#   encrypt(text,shift)
# elif direction =="decode":  
#   decrypt(text,shift)
  

def best(text,shift,direction):
    word=""
    for i in text:
        if i not in alphabet:
            word+=i
            continue
        if direction=="decode":
            shift*=-1
        new_letter_index=alphabet.index(i)+shift
        shift=abs(shift)
        while new_letter_index > 25 or new_letter_index < 0 :
            if new_letter_index > 25:
                new_letter_index-=26  
            elif new_letter_index < 0:
                new_letter_index+=26
        word+=alphabet[new_letter_index]    
    print(f"this is the decrypted word : {word}") 

answer="yes"
while answer == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    best(text=text,shift=shift,direction=direction)
    answer=input("Do you want to do it again: ").lower()
    if answer=="no":
        print("Good Bye")
        break



