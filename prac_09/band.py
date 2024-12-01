"""
CP1404 Zac Maltby
Band Class
Estimated: 20 mins
"""

class Band:
    """Band Class"""
    def __init__(self, name):
        """Initialize Band Class"""
        self.name = name
        self.musicians = []

    def __repr__(self):
        """Representation of a Band"""
        musician_string = ', '.join(str(musician) for musician in self.musicians)
        return musician_string

    def add(self, new_musician):
        """Add a new musician"""
        self.musicians.append(new_musician)

    def play(self):
        """Use play method from musician class to play"""
        return '\n'.join([musician.play() for musician in self.musicians])