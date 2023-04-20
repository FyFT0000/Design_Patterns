""" Scenario: We receive an integer value and use diferent handlers to find out its range. """

class Handler: #Abstract handler
    """ Abstract Handler """
    def __init__(self, successor) -> None:
        self._successor = successor #Define who is the next handler
    def handle(self, request):
        handled = self._handle(request) #If handled, stop here
        #Otherwise, keep going
        if not handled:
            self._successor._handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass')

class ConcreteHandler1(Handler): #Inherits from the abstract handler
    """ Concrete handler 1 """
    def _handle(self, request):
        if 0 < request <= 10: #Provide a condition for handling
            print(f'Request {request} handled in handler 1')
            return True #Indicates that the request has been andled
class DefaultHandler(Handler): #Inherits from the abstract handler
    """ Default handler """
    def _handle(self, request):
        """ If there is no handler available """
        #No condition chechin since this is a default handler
        print(f'Enf of chain, no handler for {request}')

class Client: #Using handler
    def __init__(self) -> None:
        #Create handler and use them in a sequence you want
        self.handler = ConcreteHandler1(DefaultHandler(None))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)

#Create a client
c = Client()

#Create request
requests = [2, 5, 30]

#Send the request
c.delegate(requests)

