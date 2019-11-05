import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.core.window import Window


#Window.clearcolor = (0.2,.79,0.53,1)


class DemoWindow(Screen):
    pass   

class WatWindow(Screen):
    watscore = 0
               
    def btnadd(self, value):
        if value == "down":
            self.WatWindow.watscore +=1
                      
         
    def btnmin(self,value):
        if value == "down":
            self.watscore +=0
    
    def btnthree(self,value):
        if value == "down":
            self.watscore +=2
    
    print(watscore)

            
class ResultWindow(Screen):
    print("Watscore")
    

class HomeScreen(ScreenManager):
    pass

kv = Builder.load_file("peds.kv")

class PedsMain(App):
    def build(self):
        self.title = "Withdrawal Assessment Tool"
        return kv


if __name__ == "__main__":
    PedsMain().run()