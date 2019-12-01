"""
Class MyFrame is the VIEW for a simple temperture conversion program
that exemplifies the Model/View/Controller architecture.
This View class is a tkinter.Frame that contains an input box,
three Buttons and a Label. Two of the buttons perform the conversion
and the third allows the user to quit the application.
The input box allows the user to enter the temperature.
The Label displays the converted temperature.
"""
import tkinter

class ViewTemp(tkinter.Frame):
    """ View class for temp conversion program
    One ViewTemp object represents the frame shown in the screen
    """

    root = tkinter.Tk()
    root.title("Temperature Conversion")

    def __init__(self, controllerTemp):
        """
        Places the controls onto the Frame.
        """
        tkinter.Frame.__init__(self)
        self.pack()
        self.controllerTemp = controllerTemp
        # line above ...
        # saves a reference to the controller so that we can call methods
        # on the controller object when the user generates events
        self.createWidgets()

    def createWidgets(self):
        """ Instantiates all of the widgets and places them onto the frame """
        self.inputTemp = tkinter.Entry()
        self.inputTemp.insert(0, "Enter temperature")
        self.inputTemp.pack({"side": "left"})

        #set up the convert to F Button
        self.toF_button = tkinter.Button(self)
        self.toF_button["text"] = "Convert to F"
        self.toF_button["command"] = self.controllerTemp.toF_buttonPressed
        self.toF_button.pack({"side": "left"})

        #set up the convert to C Button
        self.toC_button = tkinter.Button(self)
        self.toC_button["text"] = "Convert to C"
        self.toC_button["command"] = self.controllerTemp.toC_buttonPressed
        self.toC_button.pack({"side": "left"})

        #set up the quit Button
        self.quitButton = tkinter.Button(self)
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] = self.quit
        # the statement above attaches the event handler self.quit() to the quitButton
        self.quitButton.pack({"side": "left"})

        #set up the Label
        self.labelForOutput = tkinter.Label(self)
        self.labelForOutput["text"] = 0
        self.labelForOutput.pack({"side": "bottom"})