from kivy.app import App
from kivy.uix.button import Button


class Test0032(App):
    def build(self):
        return Button(text="Budapest")

if __name__ == '__main__':
    Test0032().run()