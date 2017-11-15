from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from random import random

from kivy.properties import NumericProperty


class MyWidget(Widget):
    cx = NumericProperty(0)
    cy = NumericProperty(0)

    def on_touch_down(self, touch):
        self.cx = touch.pos[0]
        self.cy = touch.pos[1]


class Test0144(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    Test0144().run()