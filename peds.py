import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.widget import Widget


#Window.clearcolor = (0.2,.79,0.53,1)

class HomeScreen(Screen):
    pass
class DemoScreen(Screen):
    pass   

class WatScreen(Screen):
    pass
            
class ResultScreen(Screen):
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
    
if __name__ == "__main__":
    PedsMain().run()