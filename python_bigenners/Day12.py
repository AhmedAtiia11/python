import random
def play():
    print("Welcome to the guessing game")
    print("guess number between 0 to 100")
    def num():
        num=random.randint(0,100)
        return num

    def func(attemp,number):
        # global attemp
        # global number
        while attemp > 0:
            print(f"you have {attemp} attemps to guess the number")
            user=int(input("Please enter your number: "))
            if user > number:
                print("Too high")
            elif user == number:
                print("you win")
                break
            else:
                print("Too Low")
            attemp-=1

    if input("Choose the level you want to play 'easy' or 'hard': ") == "e":
        attemp=10
        number=num()
        print(number)
        func(attemp,number)
    else:
        attemp=5
        number=num()                        
        print(number)
        func(attemp,number)

    if input("Do you want to play again (y or n) : ") =="y":
        play()

play()