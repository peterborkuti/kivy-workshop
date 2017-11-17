from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class MyWidget(BoxLayout):

    def validate(self, instance):
        popup = Popup()
        popup.auto_dismiss=False

        closeButton = Button(text='Close popup')
        closeButton.bind(on_press = popup.dismiss)

        content = BoxLayout()
        content.add_widget(Label(text="Hello"))
        content.add_widget(closeButton)

        popup.add_widget(content)
        popup.open()


class Test0500(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    Test0500().run()