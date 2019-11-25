"""
We need to add three things to class MyFrame:

i) a counter that starts at 0, gets incremented every time the user clicks
the incrementButton and whose current value is displayed in the labelForOutput.

ii) code that will be executed when the user clicks the incrementButton.
This is called an event handler or a callback method.

iii) code that will be executed when the user clicks the quitButton.

The following version of class MyFrame contains all three of these things:

"""

import tkinter

class MyFrame(tkinter.Frame):

    """
    class MyFrame is a tkinter.Frame that contains two Buttons and a Label.
    One Button increments a counter and the other Button quits.
    The Label is used to give the user information.
    """

    def __init__(self):
        """
        Places the controls onto the Frame.
        """
        tkinter.Frame.__init__(self)   # initializes the superclass

        # initialize the counter
        self.counter = 0
        self.pack()   #  required in order for the Buttons to show up properly

        #set up the increment Button
        self.incrementButton = tkinter.Button(self)
        self.incrementButton["text"] = "Increment"
        self.incrementButton["command"] = self.addOne
        # the statement above attaches the event handler addOne() to the incrementButton
        self.incrementButton.pack({"side": "left"})

        #set up the quit Button
        self.quitButton = tkinter.Button(self)
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] = self.quit
        # the statement above attaches the event handler self.quit() to the quitButton
        self.quitButton.pack({"side": "left"})

        #set up the Label
        self.labelForOutput = tkinter.Label(self)
        self.labelForOutput["text"] = 0
        self.labelForOutput.pack({"side": "left"})

    def addOne(self):
        self.counter = self.counter + 1
        self.labelForOutput["text"] = self.counter