from kivy.app import App
import sqlite3
import time
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

now=time.time()


class MyApp(App):
    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical', size_hint=(1,1))
        self.lbl1 = Label(text="Введіть дату", size_hint=(1,1), )
        layout.add_widget(self.lbl1)
        self.txt1 = TextInput(text='', multiline=False)
        self.btn1 = Button(text="Відлік")
        self.btn1.bind(on_press=self.buttonClicked)
        layout.add_widget(self.txt1)
        layout.add_widget(self.btn1)
        return layout
    
    
    def buttonClicked(self,btn):
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS datums(id INTEGER PRIMARY KEY AUTOINCREMENT, title text, datum real)""")
        sql = "INSERT INTO datums(title, datum) VALUES (?, ?)"
        cursor.execute(sql, ['тест1', self.txt1.text])
        print(cursor.fetchall())
        conn.commit()
        conn.close()
        
    class TestApp(App):
      def build(self):
        return MyApp()
        

if __name__ == '__main__':
    MyApp().run()
