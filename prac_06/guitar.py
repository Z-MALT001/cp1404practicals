"""Guitar Program
Estimated Time to Complete: 30 minutes
Time of start: 10:04am
TIme of Completion: am
Actual Time of Completion: minutes
"""


class Guitar:
    """Guitar Class"""
    def __init__(self, name='', year=0, cost=0.0):
        """Initialise Guitar Class"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Display guitar components"""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self, current_year):
        """Get guitar age"""
        return current_year - self.year

    def is_vintage(self):
        """Determine if guitar is vintage"""
        age = self.get_age(self.year)
        if age > 50:
            return True
        else:
            return False
