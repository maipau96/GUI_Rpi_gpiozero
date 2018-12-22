from tkinter import *
from gpiozero import MCP3008

pot = MCP3008(channel=0)

class App(Tk):
    
    def on_exit(self):
        self.destroy()

    def counting(self, counter):
        if (self.textonbtn == "STOP"):
            self.counter = format(pot.value, '.2f')
            self.lbl.config(text = self.counter)
            self.after(1000, self.counting, self.counter)

    def btnclickfunc(self):
        if (self.textonbtn == "READ"):
            self.textonbtn = "STOP"
            self.btn.config(text = self.textonbtn)
            self.after(1000, self.counting, self.counter)
            
        else:
            self.textonbtn = "READ"
            self.btn.config(text = self.textonbtn)
            self.lbl.config(text = self.counter)
        
        
    def __init__(self):
        Tk.__init__(self)
        self.title("New Window")
        self.geometry("450x200")
        self.protocol("WM_DELETE_WINDOW", self.on_exit)
        
        #variables
        self.textonbtn = "READ"
        self.counter = format(pot.value, '.2f')

        #arrangement of label & button
        self.intro = Label(self, text = "Toggle the button to read analog value")
        self.intro.grid(padx = 100, pady = 0)
        self.lbl = Label (self, text = self.counter )
        self.lbl.grid(padx = 150 , pady = 40)
        self.btn = Button(self, text=self.textonbtn, command = self.btnclickfunc)
        self.btn.grid(padx=150, pady=10)


if __name__ == '__main__':
    App().mainloop()
