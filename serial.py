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
        """ Constructor function for SerialGenerator
            Setting start attribute counter to 0 if start = undefined
            Setting increment counter to start
        """
        self.start = start
        self.increment = start
    
    def generate(self):
        """ Returns next generated serial number """
        self.increment += 1
        return self.increment - 1

    def reset(self):
        """ Reset serial number to start """
        self.increment = self.start