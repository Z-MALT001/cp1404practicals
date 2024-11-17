"""
Prac 8, Zac Maltby
Started: 17/11/2024
Predicted Completion: 30 minutes
"""

from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.609


class ConvertMilesKmApp(App):

    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self):
        value = self.get_valid_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def increment_input(self, change):
        current_value = self.get_valid_miles()
        new_value = current_value + change
        self.root.ids.input_miles.text = str(new_value)
        self.handle_calculation()

    def get_valid_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


ConvertMilesKmApp().run()
