from tkinter import *

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To Do List')
        self.root.geometry('650x410+300+150')

        self.label1 = Label(self.root, text = 'To Do List', font = 'Ariel 20 bold', 
        width = 10, bd = 5, bg = 'navy blue', fg = 'white')
        self.label1.pack(side = 'top', fill = BOTH)

        self.label3 = Label(self.root, text = 'Add Tasks:', font = 'Ariel 20 bold', 
        width = 20, bd = 5, fg = 'navy blue', anchor="w", justify="left")
        self.label3.place(x = 10, y= 54)

        self.txt_box = Listbox(self.root, height = 8, bd = 5, 
        width = 28, font = 'ariel, 20 italic bold')
        self.txt_box.place(x = 200, y = 110)

        self.txt = Text(self.root, bd = 5, height = 2, 
        width = 60, font = 'ariel, 10 bold')
        self.txt.place(x = 200, y = 54)

        with open("To_do_list_data.txt","r") as file:
            read = file.readlines()
            for line in read:
                read_line = line.split()
                self.txt_box.insert(END,read_line)

        self.button1 = Button(self.root, text = "Add", font = 'ariel, 20 bold italic', 
        width = 10, height = 1, bd = 5, bg = 'navy blue', fg = 'white', command = self.add )
        self.button1.place(x = 10, y = 160)

        self.button2 = Button(self.root, text = "Delete", font = 'ariel, 20 bold italic', 
        width = 10, height = 1, bd = 5, bg = 'navy blue', fg = 'white', command = self.delet )
        self.button2.place(x = 10, y = 250)

    def add(self):
        content = self.txt.get(1.0,END)
        self.txt_box.insert(END, content)
        with open("To_do_list_data.txt","a") as file:
            file.write(content)
            file.seek(0)
    
    def delet(self):
        delt = self.txt_box.curselection() 
        look = self.txt_box.get(delt)
        with open("To_do_list_data.txt","r+") as file:
            f = file.readlines()
            file.seek(0)
            for lines in f:
                items = str(look)
                if items not in lines:
                    file.write(lines)
            file.truncate()
        self.txt_box.delete(delt)
        
    
if __name__ == "__main__":
    root = Tk()
    ui = Todo(root)
    root.mainloop()