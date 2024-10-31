"""Programming Language Class"""

class ProgrammingLanguage:
    def __init__(self, name='', typing='', reflection=False, year=0):
        self.name = name
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

    def __str__(self):
        return (f"{self.name}, {self.typing} Typing, "
                f"Reflection={self.reflection}, First appeared in {self.year}")
