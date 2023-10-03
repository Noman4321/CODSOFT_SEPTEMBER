from tkinter import *
import random

class Password_Generator:
    def __init__(self,root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("300x250")
        self.root.configure(bg = "tan1")

        self.label = Label(self.root, text="Enter Length:", font="Arial, 15 bold", fg="black", bg = "tan1")
        self.label.place(x=20, y=10)

        self.label2 = Label(self.root, text="Enter Complexity (1 to 4):", font="Arial, 15 bold", fg="black", bg = "tan1")
        self.label2.place(x=20, y=60)

        self.length_input = Entry(self.root, font="Arial, 10 bold",bg = "azure")
        self.length_input.place(x=20, y=40)

        self.complexity_input = Entry(self.root, font="Arial, 10 bold",bg = "azure")
        self.complexity_input.place(x=20, y=90)

        self.button1 = Button(self.root, text="Generate Password", command=self.generate_password, width=15, font="Arial, 10 bold",fg = "white", bg = "royalblue1")
        self.button1.place(x=85, y=120)

        self.password_text = Label(self.root, text="Password: ", font="Arial, 15 bold", fg="black", bg = "tan1")
        self.password_text.place(x=20, y=160)

        self.generate_password_text = Label(self.root, text="", font="Arial, 10 bold", fg="blue4", bg = "tan1")
        self.generate_password_text.place(x=130, y=165)

    def generate_password(self):
        upcase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowcase_letters = upcase_letters.lower()

        digits = "0123456789"

        special_char = "~`!@#$%^&*()_-+={}[]\|:;\"',<.>?/"

        complexity = self.complexity_input.get()

        all = ""

        if complexity == "1":
            all += lowcase_letters
        elif complexity == "2":
            all += lowcase_letters
            all += upcase_letters
        elif complexity == "3":
            all += lowcase_letters
            all += upcase_letters
            all += digits
        elif complexity == "4":
            all += lowcase_letters
            all += upcase_letters
            all += special_char
            all += digits
        else:
            raise ValueError("Error! Invalid Input")

        length = int(self.length_input.get())
        generated_password = "".join(random.sample(all, length))

        self.generate_password_text.config(text=generated_password)

if __name__ == "__main__":
    root = Tk()
    psword_generator = Password_Generator(root)
    root.mainloop()