def capitalizeEachWord(inputS):
    # split string into a list of words     
    listOfWords = inputS.split()
    # capitalize each word in the listOfWords list     
    for i in range(len(listOfWords)):
        listOfWords[i] = listOfWords[i].capitalize()
    # rejoin listOfWords into a string     
    result = ''
    for word in listOfWords:
        result = result + word + ' '
    return result


print(capitalizeEachWord('hello world Whats up With you?'))

from random import randrange

class Die:
  def __init__(self):
    self.value = 1

  def __str__(self):
    return "This die has value : " + str(self.value)

  def roll(self):
    self.value = randrange(1,7)

if (__name__ == "__main__"):
    '''test program'''
    # create 2 die objects
    die1 = Die()
    die2 = Die()

    for i in range(10):
      die1.roll()
      die2.roll()
      print(die1, die2)
      print("sum = ", die1.value + die2.value)
