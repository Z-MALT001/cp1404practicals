"""Programming Language Class"""

class ProgrammingLanguage:
    def __init__(self, name='', typing='', reflection=False, year=0):
        """Initialise ProgrammingLanguage class"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if programming language is dynamic"""
        if self.typing == 'Dynamic':
            return True
        elif self.typing == 'Static':
            return False
        else:
            return "Invalid type"

    def __str__(self):
        """Display programming language components"""
        return (f"{self.name}, {self.typing} Typing, "
                f"Reflection={self.reflection}, First appeared in {self.year}")
