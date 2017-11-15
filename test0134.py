from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from kivy.properties import NumericProperty


class MyWidget(Widget):

    r = NumericProperty(0)




class Test0134(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    Test0134().run()