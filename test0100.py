from kivy.app import App
from kivy.uix.widget import Widget


class MyWidget(Widget):
    pass


class Test0100(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    Test0100().run()