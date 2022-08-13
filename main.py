from kivy.app import App
import sqlite3
import time
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

now=time.time()
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS datums_(id INTEGER PRIMARY KEY AUTOINCREMENT, title text, datum real)""")

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
        sql = "INSERT INTO datums(title, datum) VALUES (?, ?)"
        cursor.execute(sql, ['тест1', self.txt1.text])
        conn.commit()
        print(cursor.fetchall())
        
        # sql1 = "UPDATE datums SET title = ? WHERE id = ?;"
        # cursor.execute(sql1, ['тест111', 6])
        # conn.commit()
        
        
        #CREATE - создать таблицу
        #SELECT - получить записи
        #UPDATE - обновить записи
        #INSERT - вставить новую записи
        
        #FROM - указать имя таблицы
        #WHERE - условие
        #ORDER BY - сортировка (ASK(0, 1, 2, ...)/DESC(100, 99, 98, ...))
        #GROUP BY - групировка по условию
        
        print("Here's a listing of all the records in the table:")
        for row in cursor.execute("SELECT * FROM datums ORDER BY title"):
            print(row)
        conn.close()
        
        def add_more(self):
            self.clear_widgets(self.txt1)
        

if __name__ == '__main__':
    MyApp().run()
