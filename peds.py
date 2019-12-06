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

#setup logins variable
pickle_in = open("logins","rb")
logins = pickle.load(pickle_in)

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
    def build(self):
        self.title = "Readmission Prevention"
        return kv
    #this function is what will allow the buttons to change screens
    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current= screen_name 
    
    def loginbtn(self):
        if username == logins[0] and password == logins[1]:
            print("yay!")
        else:
            print("oops")
   
    #trying to get a score
    def __init__(self):
        super(PedsMain, self).__init__()
        self.watscore = 0

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