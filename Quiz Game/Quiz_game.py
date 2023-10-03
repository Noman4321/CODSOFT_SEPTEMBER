import pickle
import os
import time

class MCQs:

    total_score = 0
    wrong_answer = 0
    no_of_question = 0
    obtained_score = 0

    def __init__(self,question,op1,op2,op3,op4,right_option):
        self.question = question
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.op4 = op4
        self.right_option = right_option
    
    def display(self):
        print(self.question)
        print(f"1- {self.op1}           2- {self.op2}")
        print(f"3- {self.op3}           4- {self.op4}")

    def get_answer(self):
        return self.right_option
    
    def check_the_answer(self,answer):
        MCQs.total_score += 5
        if(self.right_option == answer):
            print("Correct")
            MCQs.no_of_question += 1
            MCQs.obtained_score += 5
        else:
            print("False")
            MCQs.wrong_answer += 1
    
    @staticmethod
    def check_result():
        average = MCQs.no_of_question/2
        if(average % 2 == 0):
            if(MCQs.wrong_answer < average):
                print("Congratulations! You have passed the test")
            else:
                print("Oops! You are fail")
        else:
            if(MCQs.wrong_answer <= int(average)):
                print("Congratulations! You have passed the test")
            else:
                print("Oops! You are fail")
        
        MCQs.total_score = 0
        MCQs.obtained_score = 0
        MCQs.no_of_question = 0
        MCQs.wrong_answer = 0

if __name__ == "__main__":
    while True:
        os.system('cls')
        print("Enter your choice: ")
        print("1- Add a question")
        print("2- Delete all the previous questions")
        print("3- Display the questions")
        print("4- Start a test")
        print("5- Exit")

        choice = int(input())
        if choice == 1:
            while True:
                os.system('cls')
                question = input("Enter the question : ")
                option1 = input("Option 1 : ")
                option2 = input("Option 2 : ")
                option3 = input("Option 3 : ")
                option4 = input("Option 4 : ")
                right_option = int(input("Right Option No: "))
                ques = MCQs(question,option1,option2,option3,option4,right_option) 
                with open("Quiz_game_data.pickle","ab") as f:
                    pickle.dump(ques,f)
                c = input("Enter \'t\' to add another question and \'m\' for menu : ")
                if(c == "t"):
                    continue
                elif(c== "m"):
                    break
                
        elif choice == 2:
            os.system('cls')
            with open("Quiz_game_data.pickle","wb") as f:
                f.truncate()
            print("Data removed from file.")
            c = input("Press \"m\" for menu and \"e\" for exit : ")
            if(c == "e"):
                exit()
            elif(c == "m"):
                continue

        elif choice == 3:
            os.system('cls')
            count = 1
            with open("Quiz_game_data.pickle","rb") as f:
                try:
                    while True:
                        question = pickle.load(f)
                        print(f"Question {count} :")
                        count += 1
                        question.display()
                        print(f"Answer : {question.get_answer()}\n")
                except EOFError:
                    c = input("Press \"m\" for menu and \"e\" for exit : ")
                    if(c == "e"):
                        exit()
                    elif(c == "m"):
                        continue            

        elif choice == 4:
            print("Quiz Game (each Question hold 5 marks)".center(50,'-'))
            count = 1
            with open("Quiz_game_data.pickle","rb") as f:
                try:
                    while True:
                        os.system('cls')
                        question = pickle.load(f)
                        print(f"Question {count}")
                        count = count + 1
                        question.display()
                        answer = int(input("Enter option no. : ")) 
                        question.check_the_answer(answer)
                        print("")
                        time.sleep(2.5)
                except EOFError:
                    print("Test Over")
                    print(f"Total score : {MCQs.total_score}")
                    print(f"Your score : {MCQs.obtained_score}")
                    MCQs.check_result()
                    c = input("Press m for menu and e for exit : ")
                    if(c == "e"):
                        exit()
                    elif(c == "m"):
                        continue

        elif choice == 5:
            exit()
            
        else:
            print("Please choose the right option.")
            break