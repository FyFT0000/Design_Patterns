""" Scenario: Creating menu and submenu items, and display this using the composite patter. """

class Component(object):
    """ Abstract class """

    def __init__(self, *args, **kwargs) -> None:
        pass

    def component_function(self):
        pass


class Child(Component): #Inherits from the abstract class, Component
    """ Concrete class """

    def __init__(self, *args, **kwargs) -> None:
        Component.__init__(self, *args, **kwargs)

        #This is where we store the name of your child item.
        self.name = args[0]

    def component_function(self):
        #print the name of the child itme here.
        print(f'{self.name}')

class Composite(Component): #Inherits from the abstract class, Components.
    """ Concrete class and maintains the tree recursive structure """

    def __init__(self, *args, **kwargs) -> None:
        Component.__init__(*args, **kwargs)

        #This is where we store the name of the composite objet
        self.name = args[0]

        #This is where we keep our child items
        self.children = []

    def append_child(self, child):
        """ Method to add a new child item """
        self.children.append(child)

    def remove_child(self, child):
        """ Method to remove a child """
        self.children.remove(child)

    def component_function(self):
        #Print the name of the composit objet
        print(f'{self.name}')

        #Iterate through the child objets and invoke their component
        for i in self.children:
            i.component_function()

#Build a composite submenu 1
sub1 =  Composite('submenu 1')
#Create a new child sub_menu 11
sub11 = Child('sub_menu 11')
#Create a new child sub menu 12
sub12 = Child('sub_menu 12')

#Add the sub_menu 11 to submenu 1
sub1.append_child(sub11)
#Add the sub_menu 12 to submenu 1
sub1.append_child(sub12)

#Build a top level compsite menu.
top = Composite('top_menu')
#Build a submenu 2 that is not a composite
sub2 = Child('submenu 2')
#Add the composite submenu 1 to the top-level compsite menu
top.append_child(sub1)
#Add the plain submeni 2 to the top-level composite menu
top.append_child(sub2)

#Lets test if our Composite patter works!
top.component_function()