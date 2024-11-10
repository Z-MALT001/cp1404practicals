"""Project Class"""


class Project:
    """Project Class"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise Project"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = int(completion_percentage)

    def __repr__(self):
        """Return a string representation of the object."""
        return (f"{self.name.title()}, start: ({self.start_date}), priority {self.priority}, "
                f"estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%")

    def line_format(self):
        """Format project's line."""
        return f"{self.name}\t{self.start_date}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}"

    def is_complete(self):
        """Check if project is complete."""
        return self.completion_percentage == 100
