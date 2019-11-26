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
     class MyFrame is the VIEW for a simple program that exemplifies the
     Model/View/Controller architecture. This View class is a tkinter.Frame
     that contains two Buttons and a Label. One Button increments a counter
     and the other Button quits. The Label displays the current value of the counter.
     Notice that the View never contains a reference to the Model,
     but it does contain a reference to the Controller.
    """

    def __init__(self, controller):
        """
        Places the controls onto the Frame.
        """
        tkinter.Frame.__init__(self)
        self.pack()
        self.controller = controller
        # line above ...
        # saves a reference to the controller so that we can call methods
        # on the controller object when the user generates events

        #set up the increment Button
        self.incrementButton = tkinter.Button(self)
        self.incrementButton["text"] = "Increment"
        self.incrementButton["command"] = self.controller.incButtonPressed
        self.incrementButton.pack({"side": "left"})

        #set up the decrement Button
        self.decrementButton = tkinter.Button(self)
        self.decrementButton["text"] = "Decrement"
        self.decrementButton["command"] = self.controller.decButtonPressed
        self.decrementButton.pack({"side": "left"})

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