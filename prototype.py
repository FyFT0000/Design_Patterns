import copy

class Prototype:
    def __init__(self):
        self._objets = {}

    def register_objet(self, name, obj):
        """ Register an objet """
        self._objets[name] = obj

    def unregister_objet(self, name):
        """ Unregister an objet """
        del self._objets[name]

    def clone(self, name, **attr):
        """ Clone a registered objet and update its atributes """
        obj = copy.deepcopy(self._objets.get(name))
        obj.__dict__.update(attr)
        return obj

class Car:
    def __init__(self):
        self.name = 'Skylark'
        self.color = 'Red'
        self.options = 'Ex'
    def __str__(self) -> str:
        return '{} | {} | {}'.format(self.name, self.color, self.options)

c = Car()
prototype = Prototype()
prototype.register_objet('skylark',c)

c1 = prototype.clone('skylark')

print(c)
print('------')
print(c1)
