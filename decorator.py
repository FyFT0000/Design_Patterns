""" Scenario: Function displayin a Hello Wolrd message. And wants to add aditional features to decorate the text, like <blink>. """

from functools import wraps

def make_blink(function):
    """ Defines the decorator """

    #This makes the decorator transparent in terms of its name an docsting.
    @wraps(function)

    #Define the inner function
    def decorator():
        """ The decorator function """
        #Grab the return value of the function beaing decorated.
        ret = function()

        #Add new functionality to the function being decorated.
        return '<blink>' + ret + '<blink>'
    
    return decorator

#Aply the decorator here!
@make_blink
def hello_world():
    """ Original Function! """
    return 'Hello World!'


print(hello_world())

print(hello_world.__name__)
print(hello_world.__doc__)