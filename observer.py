""" Scenario: Keep track of the core temperature of reactors at a power plant, and if there is a change in the core temperature, registered observers must be notified. """

class Subjet(): #Represents waht is being observed

    def __init__(self) -> None:
        self._observers = [] #This where reference to all the observers are being capt. Note that this is a one-to-many relationship.

    def attach(self, observer):
        #If the observer is not already in the observer list append the observer to the list.
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        #Simply remove the observer.
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:#For all the observers in the list.
            if modifier != observer: #Don't notify the observer who is actualy updating the temperature.
                observer.update(self) #Alert the observers!.

class Core(Subjet): #Inherits from the Subjet class
    def __init__(self, name='s'):
        Subjet.__init__(self)
        self._name = name #Set the name of the core
        self._temp = 0 #Initialize the temperature of the core
    
    @property #Getter that gets the core temperature
    def temp(self):
        return self._temp
    
    @temp.setter #Setter that set the core temperature
    def temp(self, temp):
        self._temp = temp
        #Notify the observers whenever somebody changes the core temperature
        self.notify()

class TempViewer:
    def update(self, subjet): #Alert method that is invoked wen the 
        print(f'Temperature Viewer: {subjet._name} has Temperature: {subjet._temp}')

#Create the subjet
c1 = Core('Core 1')
c2 = Core('Core 2')

#Create the observers
v1 = TempViewer()
v2 = TempViewer()

#Attach the observers to the first core
c1.attach(v1)
c1.attach(v2)

#Change the temperature of our first core
c1.temp = 80
c1.temp = 90


