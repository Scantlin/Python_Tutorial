from tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)
        
        self.hello = Button(frame, text="You", fg="yellow", command=self.hello)
        self.hello.pack(side=RIGHT)
        
        self.HI = Button(frame, text='Exit', fg='red', command=self.Quit)
        self.HI.pack(side="top")
        
    def say_hi(self):
        print("hi there, everyone!")
    
    def hello(self):
        frame = Label(root,  text="I love you")
        frame.pack()
        
    def Quit(self):
        root.destroy()
        
root = Tk()
root.title("You")
root.resizable(False, False)
app = App(root)

root.mainloop()