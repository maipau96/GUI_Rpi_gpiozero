from tkinter import *
from gpiozero import LED


l1 = LED(17)
l2 = LED(18)
l3 = LED(27)
l4 = LED(22)
l5 = LED(25)
l6 = LED(12)
l7 = LED(13)
l8 = LED(19)

class App(Tk):
    
    def on_exit(self):
        self.destroy()
    
    def btnclickfunc(self):
        if (self.textonbtn == "ON"):
            self.textonbtn = "OFF"
            self.btn.config(text = self.textonbtn)

            l1.on()
            l2.on()
            l3.on()
            l4.on()
            l5.on()
            l6.on()
            l7.on()
            l8.on()
        else:
            self.textonbtn = "ON"
            self.btn.config(text = self.textonbtn)
            l1.off()
            l2.off()
            l3.off()
            l4.off()
            l5.off()
            l6.off()
            l7.off()
            l8.off()
        
        
    def __init__(self):
        Tk.__init__(self)
        
        #window title
        self.title("New Window")
        
        #window size
        self.geometry("400x200")
        
        #window exit on exit button click
        self.protocol("WM_DELETE_WINDOW", self.on_exit)
        
        #variables
        self.textonbtn = "ON"

        #label arrangement
        self.lbl = Label (self, text="Toggle the button to turn on/off LED")
        self.lbl.grid(padx=100, pady=0)
        
        #button arrangement
        self.btn = Button(self, text=self.textonbtn, command = self.btnclickfunc)
        self.btn.grid(padx=150, pady=50)


if __name__ == '__main__':
    #running GUI
    App().mainloop()
