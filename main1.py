import sqlite3
 
conn = sqlite3.connect("mydatabase.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()


# # import Kivy
# import kivy
# import random
# import time

# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from datetime import datetime

# class MyApp(App):
#   # layout
#     def build(self):
#         layout = BoxLayout(padding=10, orientation='vertical')
#         btn1 = Button(text="OK")
#         btn1.bind(on_press=self.buttonClicked)
#         layout.add_widget(btn1)
#         self.lbl1 = Label(text="test")
#         layout.add_widget(self.lbl1)
#         self.txt1 = TextInput(text='', multiline=False)
#         layout.add_widget(self.txt1)
#         return layout

# # button click function
#     def buttonClicked(self,btn):
#         # self.lbl1.text = "You wrote " + self.txt1.text
#         # now = "26.01.1981"
#         date_time_str = '18/09/19 01:55:19'
#         date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')
#         print ("The type of the date is now",  type(date_time_obj))
#         print ("The date is", date_time_obj)
#         self.lbl1.text = str(date_time_obj.timestamp())

# # run app
# if __name__ == "__main__":
#     MyApp().run()
#  # join all items in a list into 1 big string