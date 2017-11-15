from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
import random

from kivy.properties import NumericProperty, Clock


class MyWidget(Widget):
    cx = NumericProperty(0)
    cy = NumericProperty(0)

    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)

        Clock.schedule_interval(self.move, 0)

    def move(self, timer):
        self.cx += random.randint(-1, 1)
        self.cy += random.randint(-1, 1)

    def on_touch_down(self, touch):
        self.cx = touch.pos[0]
        self.cy = touch.pos[1]


class Test0150(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    Test0150().run()