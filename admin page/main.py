import sqlite3

from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatIconButton,MDRaisedButton
from kivymd.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.graphics import Color, Line
from kivy.properties import NumericProperty
from math import cos, sin, pi
import datetime
from imports import *
from Messages import Send_Message
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screenmanager import MDScreenManager
import popup
from kivy.config import Config

Window.maximize()

db = "logs.db"

Config.set('kivy', 'exit_on_escape', '0')


def get_database_connection():
    con = sqlite3.connect(db)
    return con


class MyClockWidget(Screen, FloatLayout):
    def print_time(self, message):
        message = f"""THE {message} PAGE IS UNDER WORK RIGHT NOW PLEASE TRY AGAIN LATER,
        
IF THIS KEEPS ON HAPPENING PLEASE CONTACT SAM...

"""
        ERROR_CODE = "ACE57848-45"
        popup.Popup_messages.Erorr_Popup(self, message=message, error_code=ERROR_CODE)






class Ticks(Widget):
    def __init__(self, **kwargs):
        super(Ticks, self).__init__(**kwargs)
        self.bind(pos=self.update_clock)
        self.bind(size=self.update_clock)

    def update_clock(self, *args):
        self.canvas.clear()
        with self.canvas:
            time = datetime.datetime.now()
            Color(0.05,1,0.05)
            Line(points=[self.center_x, self.center_y, self.center_x+0.8*self.r*sin(pi/30*time.second), self.center_y+0.8*self.r*cos(pi/30*time.second)], width=1, cap="round")
            Color(1,1,1)
            Line(points=[self.center_x, self.center_y, self.center_x+0.7*self.r*sin(pi/30*time.minute), self.center_y+0.7*self.r*cos(pi/30*time.minute)], width=2, cap="round")
            Color(0.5,0.5,0.5)
            th = time.hour*60 + time.minute
            Line(points=[self.center_x, self.center_y, self.center_x+0.5*self.r*sin(pi/360*th), self.center_y+0.5*self.r*cos(pi/360*th)], width=3, cap="round")


    def currenttime(self,dt):
        import datetime
        dateandtime = datetime.datetime.now()
        currentmonth = str(dateandtime.month)
        currentdate = str(dateandtime.day)
        currentyear = str(dateandtime.year)
        currenthour = str(dateandtime.hour)
        currentminute = str(dateandtime.minute)
        totaldatetime = (currentmonth+"-"+currentdate+"-"+currentyear+" "+currenthour+":"+currentminute+" PM")
        date = str(dateandtime.date())
        hour_minute = str(dateandtime.hour)+":"+str(dateandtime.minute)
        if dateandtime.hour < 12:
            self.root.ids.timeanddate.text = currentmonth+"-"+currentdate+"-"+currentyear+" "+currenthour+":"+currentminute+" AM"
        else:
            self.root.ids.timeanddate.text = currentmonth+"-"+currentdate+"-"+currentyear+" "+currenthour+":"+currentminute+" PM"

    def on_start(self):
        Clock.schedule_interval(self.currenttime,1)


class Add_User(Screen):

    def clear_input(self):
        self.ids.fname.text = ""
        self.ids.lname.text = ""
        self.ids.email.text = ""
        self.ids.id.text = ""

    def add_user(self):
        F_NAME = self.ids.fname.text
        L_NAME = self.ids.lname.text
        EMAIL = self.ids.email.text
        ID = self.ids.id.text
        USER_TYPE = self.ids.type.text
        USER_TYPE = USER_TYPE.lower()

        aaa = F_NAME, L_NAME, EMAIL, ID, USER_TYPE
        add_user_info = ''' INSERT INTO info(fname, lname, email, id, type) VALUES(?,?,?,?,?); '''
        con = get_database_connection()
        con.execute(add_user_info, aaa)
        con.commit()
        con.close()


class System_Messages(Screen):

    def clear_input(self):
        self.ids.subject.text = ""
        self.ids.title.text = ""
        self.ids.message.text = ""

    def send_message(self):
        today = datetime.datetime.now()
        TIME = today.strftime("%m/%d/%Y, %I:%M %p")
        MESSAGE_SUB = self.ids.subject.text
        MESSAGE_TITLE = self.ids.title.text
        DATE = TIME
        MESSAGE = self.ids.message.text

        try:
            Send_Message.system_update_message(self, MESSAGE_SUB=MESSAGE_SUB, MESSAGE_TITLE=MESSAGE_TITLE, DATE=DATE, MESSAGE=MESSAGE)
            # print("['THE SYSTEM IS RUNNING A CLOUD UPDATE'.....]")
            # Cloud_Update.cloud_update(self)
            # print("['THE SYSTEM IS DONE WITH THE CLOUD UPDATE'.....]")
        except:
            print("['There Is A Error CHECK THE INTERNET CONNECTION OR CALL SAM']")
        else:
            print("Email Sent Successfully")
            #self.ids.sent_con.text = "Payment Confirmed"
            #self.ids.payment_input.text = ""

class Add_Season_Box(Screen):


    def clear_input(self):
        self.ids.user_id.text = ""
        self.ids.box_name.text = ""
        self.ids.box_s_date.text = ""
        self.ids.box_e_date.text = ""
        self.ids.box_id.text = ""

    def add_box(self):
        U_NAME = self.ids.user_id.text
        BOX_NAME = self.ids.box_name.text
        BOX_S_DATE = self.ids.box_s_date.text
        BOX_E_DATE = self.ids.box_e_date.text
        BOX_ID = self.ids.box_id.text
        BOX_HOURS = 0

        aaa = BOX_ID, BOX_NAME, BOX_S_DATE, BOX_E_DATE, U_NAME,BOX_HOURS
        add_box_info = ''' INSERT INTO season_box(box_id, box_name, box_start_date, box_end_date, created_by, box_hours) VALUES(?,?,?,?,?,?); '''
        con = get_database_connection()
        con.execute(add_box_info, aaa)
        con.commit()
        con.close()


class WindowManager(ScreenManager):
    pass




class AdminPanel(MDApp):
    def build(self):
        kv = Builder.load_file("design.kv")
        clock = MyClockWidget()
        Clock.schedule_interval(clock.ticks.update_clock, 1)
        return kv


    """def on_start(self):
        Clock.schedule_interval(self.currenttime, 1)

    def currenttime(self, dt):
        import datetime
        dateandtime = datetime.datetime.now()
        currentmonth = str(dateandtime.month)
        currentdate = str(dateandtime.day)
        currentyear = str(dateandtime.year)
        currenthour = str(dateandtime.hour)
        currentminute = str(dateandtime.minute)
        totaldatetime = (
                    currentmonth + "-" + currentdate + "-" + currentyear + " " + currenthour + ":" + currentminute + " PM")
        date = str(dateandtime.date())
        hour_minute = str(dateandtime.hour) + ":" + str(dateandtime.minute)
        if dateandtime.hour < 12:
            self.root.ids.timeanddate.text = currentmonth + "-" + currentdate + "-" + currentyear + " " + currenthour + ":" + currentminute + " AM"
        else:
            self.root.ids.timeanddate.text = currentmonth + "-" + currentdate + "-" + currentyear + " " + currenthour + ":" + currentminute + " PM"""





AdminPanel().run()