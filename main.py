import threading
import calculate
import get_voice
import kivy
from kivy.clock import mainthread
from kivy.uix.gridlayout import GridLayout
import os
from calculate import *
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.lang.builder import Builder
from kivy.uix.button import Button
#from android.permissions import request_permissions, Permission

ui_string = Builder.load_string("""
<ScreenManager>:
    CalciLayout:
        name:'calci_layout'
        
    VoiceCalciLayout:
        name:'voice_calci_layout'
        
<CalciLayout>:
    BoxLayout:
        orientation: "vertical"
        size: root.width,root.height
        
        TextInput:
            id:input
            text: "0"
            halign:"right"
            font_size:60
            size_hint:(1,.20)
        GridLayout:
            cols:4
            rows:5
            spacing:1
            
            # row 1
            Button: 
                size_hint:(.2, .2)
                font_size:60
                text:"%"
                background_normal:''
                color:0.2784313725490196,0.592156862745098,1,1
                background_color:1,1,1,1
                on_press:root.pressed('%')
            Button:
                size_hint:(.2,.2)
                font_size:60
                text:"/"
                background_normal:''
                color:0.2784313725490196,0.592156862745098,1,1
                background_color:1,1,1,1
                on_press:root.pressed("/")
            Button:
                size_hint:(.2,.2)
                font_size:60
                text:"C"
                background_normal:''
                color:0.2784313725490196,0.592156862745098,1,1
                background_color:1,1,1,1
                on_press:root.clear()
            Button:
                size_hint:(.2,.2)
                font_size:60
                text:"<-"
                background_normal:''
                color:0.2784313725490196,0.592156862745098,1,1
                background_color:1,1,1,1
                on_press:root.back()
                
            # row 2
            Button: 
                size_hint:(.2,.2)
                font_size:60
                text:"7"
                background_normal:''
                background_color: 0.054901960784313725,0.3137254901960784,0.5882352941176471,1
                on_press:root.pressed(7)
            Button:
                size_hint:(.2,.2)
                font_size:60
                text:"8"
                background_normal:''
                background_color: 0.054901960784313725,0.3137254901960784,0.5882352941176471,1
                on_press:root.pressed(8)
            Button:
                size_hint:(.2,.2)
                font_size:60
                text:"9"
                background_normal:''
                background_color: 0.054901960784313725,0.3137254901960784,0.5882352941176471,1
                on_press:root.pressed(9)
            Button:
                size_hint:(.2,.2)
                font_size:60
                text:"X"
                background_normal:''
                color:0.2784313725490196,0.592156862745098,1,1
                background_color:1,1,1,1
                on_press:root.pressed('*')
            
            # row 3
            Button: 
                size_hint:(.2,.2)
                font_size:60
                text:"4"
                background_normal:''
                background_color: 0.054901960784313725,0.3137254901960784,0.5882352941176471,1
                on_press:root.pressed(4)
            Button:
                size_hint:(.2,.2)
                font_size:60
                text:"5"
                background_normal:''
                background_color: 0.054901960784313725,0.3137254901960784,0.5882352941176471,1
                on_press:root.pressed(5)
            Button:
                size_hint:(.2,.2)
                font_size:60
                text:"6"
                background_normal:''
                background_color: 0.054901960784313725,0.3137254901960784,0.5882352941176471,1
                on_press:root.pressed(6)
            Button:
                size_hint:(.2,.2)
                font_size:60
                text:"-"
                background_normal:''
                color:0.2784313725490196,0.592156862745098,1,1
                background_color:1,1,1,1
                on_press:root.pressed('-')
            
            # row 4
            Button: 
                size_hint:(.2,.2)
                text:"1"
                font_size:60
                background_normal:''
                background_color: 0.054901960784313725,0.3137254901960784,0.5882352941176471,1
                on_press:root.pressed(1)
            Button:
                size_hint:(.2,.2)
                font_size:60
                text:"2"
                background_normal:''
                background_color: 0.054901960784313725,0.3137254901960784,0.5882352941176471,1
                on_press:root.pressed(2)
            Button:
                size_hint:(.2,.2)
                font_size:60
                text:"3"
                background_normal:''
                background_color: 0.054901960784313725,0.3137254901960784,0.5882352941176471,1
                on_press:root.pressed(3)
            Button:
                size_hint:(.2,.2)
                font_size:60
                text:"+"
                background_normal:''
                color:0.2784313725490196,0.592156862745098,1,1
                background_color:1,1,1,1
                on_press:root.pressed('+')
            
            # row 5
            Button: 
                size_hint:(.2,.2)
                font_size:50
                text:"Voice"
                background_normal:''
                background_color: 0,0.20784313725490197,0.47843137254901963,1
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.current='voice_calci_layout'
            Button:
                size_hint:(.2,.2)
                font_size:60
                text:"0"
                background_normal:''
                background_color: 0.054901960784313725,0.3137254901960784,0.5882352941176471,1
                on_press:root.pressed(0)
            Button:
                size_hint:(.2,.2)
                font_size:60
                text:"."
                background_normal:''
                background_color: 0,0.20784313725490197,0.47843137254901963,1
                on_press:root.pressed(".")
            Button:
                size_hint:(.2,.2)
                font_size:60
                text:"="
                background_normal:''
                background_color:0.2784313725490196,0.592156862745098,1,1
                on_press:root.answer()
<VoiceCalciLayout>:
#:import kivy.utils.platform
    BoxLayout:
        orientation:"vertical"
        size_hint:[1,.1]
        pos_hint:{'right':1,"top":0.98}
        
        Label:
            text:root.tips
    
    BoxLayout:
        orientation:"vertical"
        size_hint:[1,.1]
        pos_hint:{'right':1,'top':0.80}
        Label:
            id: inputs
            text:" 0 + 0 "
            #font_size:35
    
    BoxLayout:
        orientation:"vertical"
        size_hint:[1,.1]
        pos_hint:{'right':1,'top':0.70}
        Label:
            id: results
            text:" 0 "
            #font_size:35
            
    BoxLayout:
        orientation:"vertical"
        size_hint:[.2,.1]
        pos_hint:{'right':0.4,'top':.4}    
        Button:
            text: "Listen"
            background_normal:''
            background_color: 0.054901960784313725,0.3137254901960784,0.5882352941176471,1
            on_press: root.threaded_after(status=0)
    BoxLayout:
        orientation:"vertical"
        size_hint:[.2,.1]
        pos_hint:{'right':0.8,'top':.4}    
        Button:
            text: "Stop"
            background_normal:''
            background_color: 0.054901960784313725,0.3137254901960784,0.5882352941176471,1
            on_press: root.threaded_after(status=1)
    BoxLayout:
        orientation:"vertical"
        size_hint:[.1,.1]
        pos_hint:{'right':0.9,'top':.15}    
        Button:
            text: "Back"
            background_normal:''
            color:0.2784313725490196,0.592156862745098,1,1
            background_color:1,1,1,1
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current='calci_layout'
""")


class CalciLayout(Screen):
    def clear(self):
        self.ids.input.text = "0"

    def back(self):
        expression = self.ids.input.text
        expression = expression[:-1]
        self.ids.input.text = expression

    def pressed(self, button):
        expression = self.ids.input.text
        if "Error" in expression:
            expression = ""
        if expression == "0":
            self.ids.input.text = ""
            self.ids.input.text = f"{button}"
        else:
            self.ids.input.text = f"{expression}{button}"

    def answer(self):
        expression = self.ids.input.text
        try:
            self.ids.input.text = str(eval(expression))
        except:
            self.ids.input.text = "Error"


class VoiceCalciLayout(Screen):
    """def build(self):
        btn = Button(text="Start",
                     font_size="30sp",
                     size=(0, 0),
                     size_hint=(.2, .2),
                     pos=(10, 250))
        btn.bind(on_press=self.after)
        return btn"""
    tips = "NOTE:\n    This application partially supports \n     for 2 operands only!"

    def after(self, status=None):
        # user_data = Listen()
        user_data = status
        if user_data == "Listening...":
            self.ids.inputs.text = str(user_data)
            self.ids.results.text = "Wait"
        else:
            user_data = str(user_data)
            sto = calculate_the_data(user_data)
            sto = str(sto)
            self.ids.inputs.text = str(user_data)
            expression = self.ids.inputs.text
            self.ids.results.text = str(eval(expression))
            print(user_data)
            print(calculate_the_data(user_data))

    @mainthread
    def threaded_after(self, status=None):
        if status == 0:
            # Starts recording
            threading.Thread(target=self.after(status=0)).start()
        elif status == 1:
            # Stops recording
            threading.Thread(target=self.after(status=1)).start()


class ScreenManagment(ScreenManager):
    stop = threading.Event()


class VoiceCalculator(App):
    """def on_start(self):
        request_permissions([Permission.INTERNET, Permission.RECORD_AUDIO, Permission.READ_EXTERNAL_STORAGE,
                             Permission.WRITE_EXTERNAL_STORAGE])

    def on_stop(self):
        self.root.stop.set()
        exit()"""

    def build(self):
        return ScreenManagment()


VoiceCalculator().run()
