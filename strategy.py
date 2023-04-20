""" Scenario:  We offer our strategy class with a default set of behaviors, when there is the need we provide another variaton of the strategy class by dinamicaly replacing its default method with a new one. """

import types #Import the types module

class Strategy:
    """ The Strategy Pattern class """
    def __init__(self, function=None) -> None:
        self.name = "Default Strategy"
        #If a reference to a function is provided, replace the executed one.
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self): #This gets replaced by another version if another is provided
        """ The default method that prints the name of the strategy being executed """
        print(f'{self.name} is used.')

#Replacement method 1
def strategy_one(self):
    print(f'{self.name} is used to executed method 1')

#Replacement method 2
def strategy_two(self):
    print(f'{self.name} is used to executed method 2')

#Create our default strategy
s0 = Strategy()

#Execute our default strategy
s0.execute()

#Create the first variation of our default strategy by providing a 
s1 = Strategy(strategy_one)
#Set the name
s1.name = "Strategy One"
#Execute the strategy
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()


