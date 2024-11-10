"""Project Program
"""


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return a string representation of the object"""
        return (f"{self.name.title()}, start: {self.start_date}, priority {self.priority}, "
                f"estimate: {self.cost_estimate}, completion: {self.completion_percentage}%")


    def line_format(self):
        return f"{self.name}\t{self.start_date}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}"

    def is_complete(self):
        return self.completion_percentage == 100