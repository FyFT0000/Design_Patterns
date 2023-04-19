class Korean:
    """ Korean speaker """
    def __init__(self):
        self.name = 'Korean'
    def speak_korean(self):
        return 'An-neyong?'
    
class British:
    """ English speaker """
    def __init__(self):
        self.name = "British"
    #Note the different method name here!
    def sepak_english(self):
        return 'Hello!'


class Adapter:
    """ This changes the generic method name to indvidualized method na """

    def __init__(self, objet, **adapted_method):
        """ Change the name of the method """
        self._objet = objet

        #Add a new dictionary item that establishes the mapping beteen
        #For example, sepak() will be transalted to speak_korean if 
        self.__dict__.update(adapted_method)

    def __getattr__ (self, attr):
        """ Simply return the rest of attributes! """
        return getattr(self._objet, attr)
    
#List to store speacker objets
objets = []

#Create a Korean objet
korean = Korean()

#Create a British objet
british = British()

#Append the objet to the objet list
objets.append(Adapter(korean, speak=korean.speak_korean))
objets.append(Adapter(british, speak=british.sepak_english))

for obj in objets:
    print('{} says "{}"'.format(obj.name, obj.speak()))

