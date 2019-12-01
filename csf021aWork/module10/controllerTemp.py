"""
The module controllerTemp is the  CONTROLLER for an app that
follows the Model/View/Controller architecture.
When the user presses a Button on the View, this Controller calls
the appropriate methods in the Model.
The Controller handles all communication between the Model and the View.
"""

from csf021aWork.module10 import viewTemp  # the VIEW
from csf021aWork.module10 import convertTemp  # the MODEL

class ControllerTemp:
    """
    One object of the class represents the results of the temperature conversions
    when the user clicks either of the temperature conversion buttons
    """

    def __init__(self):
        """
        This starts the Tk framework up, instantiates the View (a ViewTemp object),
        and starts the event loop that waits for the user to press a Button on the View.
        """

        # instantiate the view -- a ViewTemp object
        self.view = viewTemp.ViewTemp(self)
        self.view.mainloop()

    def toF_buttonPressed(self):
        """
        Python calls this method when the user presses the to F button in the View.
        """
        t_in = float(self.view.inputTemp.get())  # get temp from user input in VIEW
        t_out = convertTemp.toF(t_in)
        self.view.labelForOutput["text"] = f"{t_in:.2f} deg C = {t_out:.2f} deg. F"

    def toC_buttonPressed(self):
        """
        Python calls this method when the user presses the to C button in the View.
        """
        t_in = float(self.view.inputTemp.get())  # get temp from user input in VIEW
        t_out = convertTemp.toC(t_in)
        self.view.labelForOutput["text"] = f"{t_in:.2f} deg F = {t_out:.2f} deg. C"

if __name__ == "__main__":
    c = ControllerTemp()