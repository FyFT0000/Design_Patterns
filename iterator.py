def count_to(count):
    """ Our iterator implementation """

    #Our list
    numbers_in_german = ['eins', 'zwei', 'drei', 'vier', 'funf']

    #Our built-in iterator
    #Create a tuple such as (1, 'eins')
    iterator = zip(range(count), numbers_in_german)

    #Iterate trough our iterable list
    #Extract the German number
    #Put them in a genearor caller number
    for position, number in iterator:
        #Returns a 'generator' containing numbers in German.
        yield number

#Test the generator returned by our iterator.
for num in count_to(3):
    print(num)
