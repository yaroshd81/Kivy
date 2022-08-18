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

Builder.load_file("my.kv")

now = time.time()
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS datums(id INTEGER PRIMARY KEY AUTOINCREMENT, title text, datum real)")
selectData = 0

# dt means delta-time
def timerUpdateDate(dt):
    now = time.time()
    if selectData > 0:
        if selectData > now:
            times = selectData - now
            times_year = times//31104000
            times_month = (times%31104000)//2592000
            times_day = ((times%31104000)%2592000)//86400
            times_hour = (((times%31104000)%2592000)%86400)//3600
            times_minute = ((((times%31104000)%2592000)%86400)%3600)//60
            times_second = ((((times%31104000)%2592000)%86400)%3600)%60
            times1 = str(times_day) + " дні/день, " + str(times_hour) + " годин(и), " + str(times_minute) + " хвилин(и), " + str(times_second) + " секунд(и)" 
            print(times1)
            print("selectData")
            print(selectData)
            test = "Залишилось:"
            sm.get_screen('second').ids.label1.text = "Залишилось:"
            sm.get_screen('second').ids.label2.text = times1
        else:
            print("_______________")
    else:
        print(selectData - now)

# call timerUpdateDate every 1.0 seconds
# Clock.schedule_interval(timerUpdateDate, 1.0)


class SecondWindow(Screen):
    def start(self):
        Clock.schedule_interval(timerUpdateDate, 1)
    for dat in cursor.execute("SELECT * FROM datums WHERE ID = (SELECT MAX(ID) FROM datums)"):
        datas = dat[2]
        datas_ = datetime.strptime(datas,"%d/%m/%Y")
        sec = datetime.timestamp(datas_)            
        times = int(round(sec - now))
        

            # while times > 0:
            #     times_year = times//31104000
            #     times_month = (times%31104000)//2592000
            #     times_day = ((times%31104000)%2592000)//86400
            #     times_hour = (((times%31104000)%2592000)%86400)//3600
            #     times_minute = ((((times%31104000)%2592000)%86400)%3600)//60
            #     times_second = ((((times%31104000)%2592000)%86400)%3600)%60
            #     if times > 0:
            #         if times> 60:
            #             if times > 3600:
            #                 if times > 86400:
            #                     if times > 2592000:
            #                         if times > 31104000:
            #                             times1 = str(times_year) + " рік/роки, " + str(times_month) + " місяць(і), " + str(times_day) + " дні/день, " + str(times_hour) + " годин(и), " + str(times_minute) + " хвилин(и), " + str(times_second) + " секунд(и)" 
            #                             self.label1_text.text = "Залишилось:"                                        
            #                             sm.get_screen('second').ids.label2.text = times1
            #                         else:
            #                             times1 = str(times_month) + " місяць(і), " + str(times_day) + " дні/день, " + str(times_hour) + " годин(и), " + str(times_minute) + " хвилин(и), " + str(times_second) + " секунд(и)" 
            #                             self.label1_text.text = "Залишилось:"
            #                             sm.get_screen('second').ids.label2.text = times1
            #                     else:                                        
            #                         times_year = times//31104000
            #                         times_month = (times%31104000)//2592000
            #                         times_day = ((times%31104000)%2592000)//86400
            #                         times_hour = (((times%31104000)%2592000)%86400)//3600
            #                         times_minute = ((((times%31104000)%2592000)%86400)%3600)//60
            #                         times_second = ((((times%31104000)%2592000)%86400)%3600)%60
            #                         times1 = str(times_day) + " дні/день, " + str(times_hour) + " годин(и), " + str(times_minute) + " хвилин(и), " + str(times_second) + " секунд(и)" 
            #                         print('1')
            #                         # self.label1_text.text = "Залишилось:"
            #                         sm.get_screen('second').ids.label2.text = times1
            #                 else:
            #                     times1 = str(times_hour) + " годин(и), " + str(times_minute) + " хвилин(и), " + str(times_second) + " секунд(и)" 
            #                     self.label1_text.text = "Залишилось:"
            #                     sm.get_screen('second').ids.label2.text = times1
            #             else:
            #                 times1 = str(times_minute) + " хвилин(и), " + str(times_second) + " секунд(и)" 
            #                 self.label1_text.text = "Залишилось:"
            #                 sm.get_screen('second').ids.label2.text = times1
            #         else:
            #             times1 = str(times_second) + "секунд(и)"
            #             self.label1_text.text = "Залишилось:"
            #             sm.get_screen('second').ids.label2.text = times1
    # pass

secondWindow = SecondWindow()

class FirstWindow(Screen):
    def change_text(self):
        sql = "INSERT INTO datums(title, datum) VALUES (?, ?)"
        cursor.execute(sql, ['тест1', self.data.text])
        conn.commit()
        cursor.fetchall()
        global selectData
        selectData = datetime.timestamp(datetime.strptime(self.data.text,"%d/%m/%Y"))
        secondWindow.start()
        # for dat in cursor.execute("SELECT * FROM datums WHERE ID = (SELECT MAX(ID) FROM datums)"):
        #     datas = dat[2]
        #     datas_ = datetime.strptime(datas,"%d/%m/%Y")
        #     sec = datetime.timestamp(datas_)
        #     times = int(round(sec - now))
        #     times1 = str(times)
            # while times > 0:
            #     times_year = times//31104000
            #     times_month = (times%31104000)//2592000
            #     times_day = ((times%31104000)%2592000)//86400
            #     times_hour = (((times%31104000)%2592000)%86400)//3600
            #     times_minute = ((((times%31104000)%2592000)%86400)%3600)//60
            #     times_second = ((((times%31104000)%2592000)%86400)%3600)%60
            #     if times > 0:
            #         if times> 60:
            #             if times > 3600:
            #                 if times > 86400:
            #                     if times > 2592000:
            #                         if times > 31104000:
            #                             times1 = str(times_year) + " рік/роки, " + str(times_month) + " місяць(і), " + str(times_day) + " дні/день, " + str(times_hour) + " годин(и), " + str(times_minute) + " хвилин(и), " + str(times_second) + " секунд(и)" 
            #                             # self.label1_text.text = "Залишилось:"
            #                             # self.label2_text.text = times1
            #                         else:
            #                             times1 = str(times_month) + " місяць(і), " + str(times_day) + " дні/день, " + str(times_hour) + " годин(и), " + str(times_minute) + " хвилин(и), " + str(times_second) + " секунд(и)" 
            #                             # self.label1_text.text = "Залишилось:"
            #                             # self.label2_text.text = times1 
            #                     else:
            #                         times_year = times//31104000
            #                         times_month = (times%31104000)//2592000
            #                         times_day = ((times%31104000)%2592000)//86400
            #                         times_hour = (((times%31104000)%2592000)%86400)//3600
            #                         times_minute = ((((times%31104000)%2592000)%86400)%3600)//60
            #                         times_second = ((((times%31104000)%2592000)%86400)%3600)%60
            #                         times1 = str(times_day) + " дні/день, " + str(times_hour) + " годин(и), " + str(times_minute) + " хвилин(и), " + str(times_second) + " секунд(и)" 
            #                         print(times1)
            #                         test = "Залишилось:"
            #                         # self.label1_text.text = "Залишилось:"
            #                         # self.label2_text.text = times1
            #                 else:
            #                     times1 = str(times_hour) + " годин(и), " + str(times_minute) + " хвилин(и), " + str(times_second) + " секунд(и)" 
            #                     # self.label1_text.text = "Залишилось:"
            #                     # self.label2_text.text = times1
            #             else:
            #                 times1 = str(times_minute) + " хвилин(и), " + str(times_second) + " секунд(и)" 
            #                 # self.label1_text.text = "Залишилось:"
            #                 # self.label2_text.text = times1
            #         else:
            #             times1 = str(times_second) + "секунд(и)"
            #             # self.label1_text.text = "Залишилось:"
            #             # self.label2_text.text = times1
            # sm.get_screen('second').ids.label2.text = times1

class WindowManager(ScreenManager):
    pass

# class Container1(FloatLayout):
#     def change_text(self):
#         print("11111111111")
#         sql = "INSERT INTO datums(title, datum) VALUES (?, ?)"
#         cursor.execute(sql, ['тест1', self.data.text])
#         conn.commit()
#         cursor.fetchall()

sm = ScreenManager()
sm.add_widget(FirstWindow(name='first'))
sm.add_widget(SecondWindow(name='second'))

class MyApp(App):
    def build(self):
        return sm


        

if __name__ == '__main__':
    MyApp().run()
