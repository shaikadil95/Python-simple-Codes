from tkinter import *

def doNothing():
    print("Adil")

root = Tk()

root.title('INTERNET WHITEBOARD USER')
root.geometry('600x200')


menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="Internet WhiteBoard", menu=subMenu)
subMenu.add_command(label="Profile", command=doNothing)
subMenu.add_command(label="Signout", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="About Us", command=doNothing)

clickMenu = Menu(menu)
menu.add_cascade(label="Help", menu=clickMenu)
clickMenu.add_command(label="About Us", command=doNothing)


from tkinter import *


class UserPage:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="START SESSION", command=self.printMessage)
        self.printButton.pack(side=LEFT)
        Button(root, text="Quit", command=quit).pack()
        
    def printMessage(self):
        print("Session started by Adil")



b = UserPage(root)
root.mainloop()
