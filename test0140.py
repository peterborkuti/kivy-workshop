from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from random import random

from kivy.properties import NumericProperty


class MyWidget(Widget):

    def on_touch_down(self, touch):
        print touch

class Test0140(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    Test0140().run()