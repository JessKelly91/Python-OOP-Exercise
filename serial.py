"""Python serial number generator."""

class SerialGenerator:        
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    def __init__(self, start=0):
        """initializer for instance of SerialGenerator, with the initial # being start

        if start is missing, it will automatically start at zero
        
        """
        self.start = start
        self.next = start


    def __repr__(self):
        """show representation of instance"""
        return f"<SerialGenerator start={self.start} next ={self.next}>"
    
    def generate(self):
        #generates and returns the next number in the sequence
        self.next += 1
        return self.next -1
        

    def reset(self):
        #reset to instances original start #
        self.next = self.start