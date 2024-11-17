"""
Prac 8, Zac Maltby
17/11/24
Predicted Completion Time: Half Hour
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label

names = ['zac', 'bob']


class ListDivider(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = names

    def build(self):
        self.title = 'THE LIST DIVIDER'
        self.root = Builder.load_string('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


ListDivider().run()
