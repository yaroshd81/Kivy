from kivy.app import App
from kivy.lang import Builder
import sqlite3
import time
from datetime import datetime
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
Clock.max_iteration = 20

Builder.load_file("1.kv")

now = time.time()
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS datums(id INTEGER PRIMARY KEY AUTOINCREMENT, title text, datum real)")
selectData = 0
conn2 = sqlite3.connect("mydatabase2.db")
cursor2 = conn2.cursor()
cursor2.execute("CREATE TABLE IF NOT EXISTS screen(id INTEGER PRIMARY KEY AUTOINCREMENT, title text, screens real)")
fscreen = 'first'

def screens_first():
  sql2 = "INSERT INTO screen(title, screens) VALUES (?, ?)"
  cursor2.execute(sql2, ['тест1','second'])
  conn2.commit()
  print('screen')
    
def timerUpdateDate(dt):
    for dat in cursor.execute("SELECT * FROM datums WHERE ID = (SELECT MAX(ID) FROM datums)"):
        datas = dat[2]
        datas_ = datetime.strptime(datas,"%d/%m/%Y")
        sec = datetime.timestamp(datas_)
        now = time.time()
        if sec > 0:
            if sec > now:
                times = int(round(sec- now))
                times_year = times//31104000
                times_month = (times%31104000)//2592000
                times_day = ((times%31104000)%2592000)//86400
                times_hour = (((times%31104000)%2592000)%86400)//3600
                times_minute = ((((times%31104000)%2592000)%86400)%3600)//60
                times_second = ((((times%31104000)%2592000)%86400)%3600)%60
                #Dimrix
                if times_day != 11:
                    times_day_ = times_day - (times_day // 10) * 10
                else:
                    times_day_ = 9
                print(times_day_)
                if times_day_ == 1:
                    timesLabel = " день "
                elif times_day_ < 5:
                    timesLabel = " дні "
                else:
                    timesLabel = " днів "
                    
                times1 = str(times_day) + timesLabel + str(times_hour) + " годин(и) \n" + str(times_minute) + " хвилин(и) " + str(times_second) + " секунд(и)" 
                #Dimrix

                # times1 = str(times_day) + " дні/день/днів, " + str(times_hour) + " годин(и), \n" + str(times_minute) + " хвилин(и), " + str(times_second) + " секунд(и)" 
                print(times1)
                print("sec")
                print(sec)
                sm.get_screen('first').ids.label1.text = "Залишилось:"
                sm.get_screen('first').ids.label2.text = times1
            else:
                print("_______________")
        else:
            print(sec - now)

class SecondWindow(Screen):
    def change_text(self):
        sql = "INSERT INTO datums(title, datum) VALUES (?, ?)"
        cursor.execute(sql, ['тест1', self.data.text])
        conn.commit()
        cursor.fetchall()
        firstWindow.start()

class FirstWindow(Screen):
  def start(self):
    Clock.schedule_interval(timerUpdateDate, 1)
  for dat in cursor.execute("SELECT * FROM datums WHERE ID = (SELECT MAX(ID) FROM datums)"):
    datas = dat[2]
    datas_ = datetime.strptime(str(datas),"%d/%m/%Y")
    sec = datetime.timestamp(datas_)            
    times = int(round(sec - now))
    Clock.schedule_interval(timerUpdateDate, 1)
        
firstWindow = FirstWindow()

class WindowManager(ScreenManager):
  pass

sm = ScreenManager()
sm.add_widget(FirstWindow(name='first'))
sm.add_widget(SecondWindow(name='second'))

class MyApp(App):
  def build(self):
    return sm


        

if __name__ == '__main__':
  MyApp().run()
