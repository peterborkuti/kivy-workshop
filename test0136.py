from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from random import random

from kivy.properties import NumericProperty


class MyWidget(Widget):

    r = NumericProperty(0)

    def pressed(self):
        self.r = random()

class Test0136(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    Test0136().run()