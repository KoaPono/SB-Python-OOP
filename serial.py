"""Python serial number generator."""

class SerialGenerator:
    """Class to create unique incrementing serial numbers.
    
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
    def __init__ (self, start=0):
        """Make a new serial generator with starting serial number"""
        self.start = start
        self.current_serial = start

    def __repr__(self):
        """Show representation."""

        return f"<SerialGenerator start={self.start} current_serial={self.current_serial}>"
    
    def generate(self):
        """Return next serial number"""
        serial = self.current_serial
        self.current_serial += 1
        return serial
    
    def reset(self):
        """Reset serial number back to starting serial number"""
        self.current_serial = self.start
    

