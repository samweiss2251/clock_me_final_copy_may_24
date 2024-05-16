from imports import *
import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class Popup_messages:


    def Payment_Popup(self, AMOUNT, receipt_number):
        self.AMOUNT = AMOUNT
        self.receipt_number = receipt_number

        popup = Popup(title='Payment Popup Screen',
                      content=Label(text=f'''Your Payment Of ${AMOUNT} Dollars Was Successfully Entered.
        Conformation Number: {receipt_number}'''))
        # Add a button to the popup screen
        # Open the popup screen
        popup.open()
        Clock.schedule_once(lambda dt: popup.dismiss(), 5)

    def S_Box_Popup(self, ID, AMOUNT, TIME, SUBB, BOX_NAME):
        self.ID = ID
        self.AMOUNT = AMOUNT
        self.TIME = TIME
        self.SUBB = SUBB
        self.BOX_NAME = BOX_NAME



        popup = Popup(title='S Box Popup Screen',
                      content=Label(text=f"""

                            ************* Season Box Hours Update *************


                                            ID: {ID}
                                            Box Name: {BOX_NAME}
                                            Adding Amount: {AMOUNT} 
                                            At:  {TIME} 
                                            Total Amount Of Hours In Season Box: 
                                                        {SUBB}


                        ============================================================
                                ...Thanks For Choosing The Clock Me System...
                        """))
        # Add a button to the popup screen
        # Open the popup screen
        popup.open()
        Clock.schedule_once(lambda dt: popup.dismiss(), 10)


    def Erorr_Popup(self, message, error_code):
        self.message = message
        self.error_code = error_code

        popup = Popup(title='Error Message',
                      content=Label(text=f'''{message} .
        Error Code: {error_code}'''))
        # Add a button to the popup screen
        # Open the popup screen
        popup.open()
        Clock.schedule_once(lambda dt: popup.dismiss(), 5)