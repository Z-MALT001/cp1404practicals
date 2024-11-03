"""Guitar Program
Estimated Time to Complete: 30 minutes
Time of start: 10:04am
TIme of Completion: 10:46am
Actual Time of Completion: 42 minutes
"""

CURRENT_YEAR = 2024


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

    def get_age(self):
        """Get guitar age"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if guitar is vintage"""
        age = self.get_age()
        if age > 50:
            return True
        else:
            return False
