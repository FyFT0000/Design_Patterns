""" Scenario: We use a house class, visitors include an HVAC specialist (visitor type 1) and an Electrician (visitor type 2). """

class House(object): #The class being visited
    def accept(self, visitor):
        """ Interface to accept a visitor """
        visitor.visit(self) #Triggers the visitin operation.

    def work_on_hvac(self, hvac_specialist):
        print(self, 'worked on by', hvac_specialist)

    def work_on_electricity(self, electrician):
        print(self, 'worked on by', electrician)#Note that we now have a reference to the electricial objet in ...

    def __str__(self) -> str:
        """ Simply return the class name when the house objet is printed """
        return self.__class__.__name__
    
class Visitor():
    """ Abstract visitor """
    def __str__(self):
        """ Simply return the class name when the Visitor objet is printed """
        return self.__class__.__name__

class HvacSpecialist(Visitor): #Inherits form the parent class Visitor.
    def visit(self, house):
        house.work_on_hvac(self) #Note that the visitor now has a reference to house class objet.

class Electrician(Visitor): #Inherits from the parent class Visitor.
    """ Concrete visitor: electrician """
    def visit(self, house):
        house.work_on_electricity(self)#Note that the visitor now has a reference to the house objet.

#Create an HVAC specialist.
hv = HvacSpecialist()

#Create an electrician.
e = Electrician()

#Create a house.
home = House()

#Let the house accept the HVAC specialist and work on the house by invoking 
home.accept(hv)

#Let the house accept the electrician specialist and work on the house by invoking 
home.accept(e)
