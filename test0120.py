from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


class MyWidget(Widget):
    pass


class Test0120(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    Test0120().run()