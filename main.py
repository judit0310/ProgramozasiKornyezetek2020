from kivy.app import App
from kivy.graphics.vertex_instructions import Line
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import BorderImage
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.base import ExceptionHandler, ExceptionManager, runTouchApp
from recyclerview import ExampleViewer
from kivy.core.window import Window

sm = ScreenManager()

from kivy.graphics import Color, Rectangle
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
data=[{'text':"cica","age":11},{'text':"cica","age":11},{'text':"cica","age":11},{'text':"cica","age":11},{'text':"cica","age":11},{'text':"kutya",'age':4}]

class TableScreen(Screen):
    def __init__(self, **kwargs):
        layout = FloatLayout(size=Window.size)

        self.rv = ExampleViewer()
        self.rv.width=Window.width
        print(Window.size)
        super(TableScreen, self).__init__(**kwargs)
        self.rv.data=data
        layout.add_widget(self.rv)
        button = Button(text='Back',size_hint =(0.7, .2))
        button.pos_hint={'center_x':0.5,'y':0}
        separator=Label(size_hint=(1,.22))
        with separator.canvas:
            Color=(0,1,1,1)
            self.rect = Rectangle(size=separator.size,
                                  pos=separator.pos)
        separator.bind(size=self._update_rect, pos=self._update_rect)
        self.add_widget(separator)
        button.bind(on_press= self.backButton)
        self.button = button
        layout.add_widget(button)
        self.layout = layout
        self.add_widget(layout)

    def backButton(self,btn):
        sm.transition.direction="right"
        sm.current ="Login"

    def _update_rect(self, instance, value):
      self.rect.pos = instance.pos
      self.rect.size = instance.size

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        layout = BoxLayout()
        super(LoginScreen, self).__init__(**kwargs)
        layout.orientation = "vertical"
        layout.opacity = 80
        layout.padding =20
        doboz = GridLayout()

        doboz.cols = 2
        doboz.add_widget(Label(text='User Name'))
        doboz.username = TextInput(multiline=False)
        doboz.add_widget(doboz.username)
        doboz.add_widget(Label(text='password'))
        passwd = TextInput(password=True, multiline=False)
        passwd.foreground_color= (1,0,1,1)
        passwd.background_color= (0,0,0,0)
        doboz.password = passwd
        doboz.add_widget(doboz.password)
        doboz.bind(pos=self.redraw, size = self.redraw)
        with doboz.canvas.before:
            # Image.source = "cica.jpeg"
            Color(1, 1, 1, 1)  # green; colors range from 0-1 instead of 0-255
            self.bg_rect = Rectangle(size=doboz.size,pos=doboz.pos,source ="cica.jpeg")
        self.doboz = doboz
        layout.add_widget(doboz)
        button = Button(text='My first button')
        button.background_down = "cica2.jpeg"
        button.background_normal = "cica.jpeg"
        button.bind(on_press= self.getDataFromFields)
        button.bind(on_touch_down=self.checkTap)
        self.button = button
        layout.add_widget(button)
        self.layout = layout
        self.add_widget(layout)
        self.bind(on_leave= self.clearInputs)

    def checkTap(self,instance,touch):
        if touch.is_double_tap:
            parent = instance.parent
            parent.remove_widget(instance)

    def clearInputs(self,message):
        self.doboz.username.text = ''
        self.doboz.password.text = ''

    def getDataFromFields(self,btn):
        username = self.doboz.username
        passwd = self.doboz.password
        if len(username.text)>0 and len(passwd.text)>0:
            if hasattr(self.layout, "errorMessage"):
                self.layout.remove_widget(self.layout.errorMessage)
            print("Username"+ username.text+", passwd:"+passwd.text)
            print(sm.screen_names)
            sm.transition.direction = "left"
            sm.current= "Data"
        else:
            print(hasattr(self.layout, "errorMessage"))
            if not hasattr(self.layout,"errorMessage"):
                errorMessage = Label(text="Invalid Credentials")
                self.layout.errorMessage = errorMessage
                self.layout.add_widget(errorMessage,index=0)



    def redraw(self,instance,value):
        self.bg_rect.size = instance.size
        self.bg_rect.pos = instance.pos



class MyApp(App):
    def build(self):
        self.root =screen = LoginScreen(name="Login")
        screen.bind(size=self._update_rect, pos= self._update_rect)
        with screen.canvas.before:
            Color(0, 1, 0, 1)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=screen.size,
                                  pos=screen.pos)
        sm.add_widget(screen)
        sm.add_widget(TableScreen(name="Data"))
        sm.current = "Login"
        return sm


    def _update_rect(self, instance, value):
      self.rect.pos = instance.pos
      self.rect.size = instance.size


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MyApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
