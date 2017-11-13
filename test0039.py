from kivy.app import App
from kivy.uix.widget import Widget


class MyWidget(Widget):
    def pressed(self, instance):
        print "Hello"


class Test0039(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    Test0039().run()