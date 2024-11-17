"""
Prac 8, Zac Maltby
Started: 17/11/2024
Predicted Completion: 30 minutes
"""

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.609


class ConvertMilesKmApp(App):

    def build(self):
        # Window.size = (1000, 500)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, value):
        value = self.get_valid_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def get_valid_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def increment_input(self, change):
        current_value = self.get_valid_miles()
        new_value = current_value + float(change)
        self.root.ids.input_numbers.text = str(new_value)


ConvertMilesKmApp().run()
