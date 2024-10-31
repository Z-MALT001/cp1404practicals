"""Programming Language Class"""

class ProgrammingLanguage:
    def __init__(self, typing='', reflection=False, year=0):
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == 'Dynamic':
            return True
        elif self.typing == 'Static':
            return False
        else:
            return "Invalid type"


