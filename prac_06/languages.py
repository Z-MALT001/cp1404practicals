"""Languages program
Estimated Time to Complete: 25 minutes
Time of start: 9:39am
TIme of Completion: 10:00am
Actual Time of Completion: 21 minutes
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
programming_languages = [python, ruby, visual_basic]
print(python)

print("The dynamically typed languages are: ")
for programming_language in programming_languages:
    if programming_language.is_dynamic():
        print(programming_language.name)
