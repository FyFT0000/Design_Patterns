""" 
Scenario: Pet shop
Only selling dogs, but now is necessary to sell cats too
 """

class Dog:
    """ A simple dog class """
    
    def __init__(self,name):
        self.name = name

    def speak(self):
        return 'Woof!'