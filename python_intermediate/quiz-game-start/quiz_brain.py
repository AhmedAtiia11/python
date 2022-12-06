class  quizbrain:
    def __init__(self,answer,user_answer,points,number):
        self.user_points=points
        self.question_number=number
        if answer == user_answer:
            print("That's right")
            self.user_points+=1
            print(f"your points are {self.user_points}/{self.question_number}")
            self.cont=True
            self.question_number+=1

        else :
            print("you are wrong")    
            print(f"your points are {self.user_points}/{self.question_number}")
            inp=input("Do you want to play again(y/n)? ")
            if inp=='n':
                self.cont=False
            else:
                self.cont=True
                self.user_points=0
                self.question_number=1 
        print("\n")        
