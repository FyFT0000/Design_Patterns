""" Scenario: We create an instance of a producer class only when its available because ony a fix number of producer objets can exists at a given time. The proxi is a Artist that check if the producer is available for a guest. """

import time

class Producer:
    """ Define the 'resource-intensive' objet to instantiate """
    def producer(self):
        print('Producer is working hard!')

    def meet(self):
        print('Producer has time to meet you now!')

class Proxy:
    """ Define the 'relatively less resource-intensive' proxi to instantiate """
    def __init__(self) -> None:
        self.occupied = 'No'
        self.producer = None
    
    def produce(self):
        """ Check if Producer is available """
        print("Artist checking if Producer is available...")

        if self.occupied == 'No':
            #If the producer is available, create a producer objet!
            self.producer = Producer()
            time.sleep(2)

            #Make the producer meet the guest!
            self.producer.meet()

        else:
            #Otherwise, don't instantiate the producer.
            time.sleep(2)
            print('Producer is busy!')

#Instantiate a Proxy first
p = Proxy()

#Make the proxy: Artist produce until Producer is vailable
p.produce()

#Change the state to 'ocupied'
p.occupied = 'Yes'

#Make the Producer produce
p.produce()


