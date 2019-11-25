"""
This main program creates a MyFrame object that contains two Buttons and a Label.

If anyone is writing an application that needs a Frame containing two Buttons and a Label,
they can just create an instance of class MyFrame and Python will put a Frame
onto the user's screen that contains two Buttons and a Label. Here is such a program:
"""
import myFrame    # contains class MyFrame
import tkinter

if __name__ == "__main__":
    root = tkinter.Tk()
    view = myFrame.MyFrame()  # puts the Frame onto the user's screen
    view.mainloop()
