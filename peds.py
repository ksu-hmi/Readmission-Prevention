import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty
from kivy.core.window import Window
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
import pickle




Window.clearcolor = (0.2,.79,0.53,1)

class LoginScreen(Screen):
    pass

class HomeScreen(Screen):
    pass
class ImageButton(ButtonBehavior,Image):
    pass
class WatScreen(Screen):
    pass
            
class ResultScreen(Screen):
    pass
class ResultScreenTwo(Screen):
    pass
class ResultScreenThree(Screen):
    pass
class WeightScreen(Screen):
    pass
 
kv = Builder.load_file("peds.kv")

class PedsMain(App):
    def __init__(self):
        self.username = ""
        self.password = ""
        #self.pickle_in = ""
        #self.logins = {}
        super(PedsMain, self).__init__()
        self.watscore = 0
        #setup logins variable
        self.pickle_in = open("logins","rb")
        self.logins = pickle.load(self.pickle_in)

    def build(self):
        self.title = "Readmission Prevention"
        return kv
    #this function is what will allow the buttons to change screens
    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current= screen_name 
    
    def loginbtn(self):
        if self.username == self.logins['atest'] and self.password == self.logins['btest']:
            print("yay!")
            print("for username you input: ",self.username)
            print("for that username we retrieved",self.logins['atest'])
            print("for password you input: ",self.password)
            print("for that password we retrieved",self.logins['btest'])
        else:
            print("oops")
            print("for username you input: ",self.username)
            print("for that username we retrieved",self.logins['atest'])
            print("for password you input: ",self.password)
            print("for that password we retrieved",self.logins['btest'])
 

        

    def btnadd(self,value):
        if value == 'normal':
            self.watscore += 0
        else:
            self.watscore +=1
    def btnmin(self,value):
        if value == 'normal':
            self.watscore += 0
        else:
            self.watscore +=0
    def btnthree(self,value):
        if value == 'normal':
            self.watscore += 0
        else:
            self.watscore += 2
    
    def resultbtn(self):
        if self.watscore < 3:
            self.change_screen("result_screen")
        elif self.watscore <= 5:
            self.change_screen("result_screentwo")
        else:
            self.change_screen("result_screenthree")
    
if __name__ == "__main__":
    PedsMain().run()