""" 
Scenario: Pet factory, incloudin dog and cat factory. And related products as dog and cat food. 
Solution:
	Abstact factory - pet factory (create objets)
	Concrete factory - dog factory and cat factory (ofthen are singleton)
	Concret product - Dog and dog food - Cat and cat foot.

We implement the abstract factory without using inheritance, beacose python is a dinamicaly typed language, and therfore does not requiered abstract clases.
 """

class Dog:
    """ One of the objets to be returned """
    
    def speak(self):
        return 'Woof!'
    def __str__(self):
        return 'Dog'
    
class DogFactory:
    """ Concrete Factory """
    
    def get_pet(self):
        """ Returns a Dog objet """
        return Dog()

    def get_food(self):
        """ Return a Dog Food objet """
        return 'Dog Food!'
        

class Cat:
    """ One of the objets to be returned """
    
    def speak(self):
        return 'Meaw!'
    def __str__(self):
        return 'Cat'
    
class CatFactory:
    """ Concrete Factory """
    
    def get_pet(self):
        """ Returns a Cat objet """
        return Cat()

    def get_food(self):
        """ Return a Cat Food objet """
        return 'Cat Food!'


class PetStore:
    """ PetStore houses our Abstract Factory """

    def __init__(self, pet_factory=None):
        """ pet_factory is our Abstract Factory"""

        self._pet_factory = pet_factory


    def show_pet(self):
        """ Utility method to display the details of the objets returned """

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print(f'Our pet is {pet}')
        print(f'Our pet says hello by {pet.speak()}')
        print(f'Its food is {pet_food}')

    

#Create a Concrete Factory
factory = DogFactory()
factory_cat = CatFactory()

#Create a pet store housing  our Abstract Factory
shop = PetStore(factory)
shop_cat = PetStore(factory_cat)

#Invoke the utility method to show the details of our pet
shop.show_pet()
shop_cat.show_pet()