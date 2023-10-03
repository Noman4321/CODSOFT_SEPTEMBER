from tkinter import *

class Calculator:
    def __init__(self, root):
        self.root = root
        self.calculation = ""
        self.root.title("Calculator")
        self.root.geometry("400x420")
        self.root.configure(bg = "grey")

        self.text_result = Text(root, height = 4, width = 44, font = 'ariel, 12 bold' ,bg = "light blue",fg = "black")
        self.text_result.grid(columnspan = 5)

        self.btn_1 = Button(root, text= "1", command = lambda: self.add_to_calculation(1), height = 3, width=10,font= "Ariel,14", bg="white", fg= "black")
        self.btn_1.grid(row = 2, column = 1)

        self.btn_2 = Button(root, text= "2", command = lambda: self.add_to_calculation(2), height = 3, width=10,font= "Ariel,14", bg="white", fg= "black")
        self.btn_2.grid(row = 2, column = 2)

        self.btn_3 = Button(root, text= "3", command = lambda: self.add_to_calculation(3), height = 3, width=10,font= "Ariel,14", bg="white", fg= "black")
        self.btn_3.grid(row = 2, column = 3)

        self.btn_4 = Button(root, text= "4", command = lambda: self.add_to_calculation(4), height = 3, width=10,font= "Ariel,14", bg="white", fg= "black")
        self.btn_4.grid(row = 3, column = 1)

        self.btn_5 = Button(root, text= "5", command = lambda: self.add_to_calculation(5), height = 3, width=10,font= "Ariel,14", bg="white", fg= "black")
        self.btn_5.grid(row = 3, column = 2)

        self.btn_6 = Button(root, text= "6", command = lambda: self.add_to_calculation(6), height = 3, width=10,font= "Ariel,14", bg="white", fg= "black")
        self.btn_6.grid(row = 3, column = 3)

        self.btn_7 = Button(root, text= "7", command = lambda: self.add_to_calculation(7), height = 3, width=10,font= "Ariel,14", bg="white", fg= "black")
        self.btn_7.grid(row = 4, column = 1)

        self.btn_8 = Button(root, text= "8", command = lambda: self.add_to_calculation(8), height = 3, width=10,font= "Ariel,14", bg="white", fg= "black")
        self.btn_8.grid(row = 4, column = 2)

        self.btn_9 = Button(root, text= "9", command = lambda: self.add_to_calculation(9), height = 3, width=10,font= "Ariel,14", bg="white", fg= "black")
        self.btn_9.grid(row = 4, column = 3)

        self.btn_0 = Button(root, text= "0", command = lambda: self.add_to_calculation(0), height = 3, width=10,font= "Ariel,14", bg="white", fg= "black")
        self.btn_0.grid(row = 5, column = 2)

        self.btn_open = Button(root, text= "(", command = lambda: self.add_to_calculation('('), height = 3, width=10,font= "Ariel,14", bg="white", fg= "black")
        self.btn_open.grid(row = 5, column = 1)

        self.btn_close = Button(root, text= ")", command = lambda: self.add_to_calculation(')'), height = 3, width=10,font= "Ariel,14", bg="white", fg="black")
        self.btn_close.grid(row = 5, column = 3)

        self.btn_plus = Button(root, text= "+", command = lambda: self.add_to_calculation('+'), height = 3, width=10,font= "Ariel,14", bg="black", fg= "white")
        self.btn_plus.grid(row = 2, column = 4)

        self.btn_minus = Button(root, text= "-", command = lambda: self.add_to_calculation('-'), height = 3, width=10,font= "Ariel,14", bg="black", fg= "white")
        self.btn_minus.grid(row = 3, column = 4)

        self.btn_mul = Button(root, text= "*", command = lambda: self.add_to_calculation('*'), height = 3, width=10,font= "Ariel,14", bg="black", fg= "white")
        self.btn_mul.grid(row = 4, column = 4)

        self.btn_divide = Button(root, text= "/", command = lambda: self.add_to_calculation('/'), height = 3, width=10,font= "Ariel,14", bg="black", fg= "white")
        self.btn_divide.grid(row = 5, column = 4)

        self.btn_equals_to = Button(root, text= "=", command = self.evaluate_calculation, height = 3, width=21,font= "Ariel,14", bg="black", fg= "white")
        self.btn_equals_to.grid(row = 6, column = 3, columnspan = 2)

        self.btn_clear = Button(root, text= "C", command = self.clear_field , height = 3, width=21,font= "Ariel,14",bg="red",fg="white")
        self.btn_clear.grid(row = 6, column = 1, columnspan = 2)


    def add_to_calculation(self,symbol):
        self.calculation += str(symbol)
        self.text_result.delete(1.0, "end")
        self.text_result.insert(1.0, self.calculation)

    def clear_field(self):
        self.calculation = ""
        self.text_result.delete(1.0, "end")

    def evaluate_calculation(self):
        try:
            result = str(eval(self.calculation))
            self.text_result.delete(1.0,"end")
            self.text_result.insert(1.0,result)
        except:
            self.clear_field()
            self.text_result.insert(1.0,"Error")

if __name__ == "__main__":
    root = Tk()
    cal = Calculator(root)
    root.mainloop()