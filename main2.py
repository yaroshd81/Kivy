from kivy.app import App
import sqlite3
import time
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

now=time.time()

class MyApp2(App):
    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')
        self.lbl2 = Label(text="Відлік")
        self.lbl3 = Label(text= "a" )
        # self.btn2 = Button(text="Назад")
        # self.btn2.bind(on_press=self.buttonClicked)
        layout.add_widget(self.lbl2)
        layout.add_widget(self.lbl3)
        # layout.add_widget(self.btn2)
        return layout

if __name__ == '__main__':
    MyApp2().run()