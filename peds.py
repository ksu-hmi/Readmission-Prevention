import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty


class DemoWindow(Screen):
    pass   

class WatWindow(Screen):
    watscore = 0
    print(watscore)
    
    def btnadd(self):
        self.watscore +=1
         
    def btnmin(self):
        self.watscore +=0
    
    def btnthree(self):
        self.watscore +=2

class ResultWindow(Screen):
    watscore = 0
    print("Watscore", watscore)
    

class HomeScreen(ScreenManager):
    pass

kv = Builder.load_file("peds.kv")

class PedsMain(App):
    def build(self):
        return kv


if __name__ == "__main__":
    PedsMain().run()