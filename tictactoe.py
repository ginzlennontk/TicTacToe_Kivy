import kivy
kivy.require('1.9.0')
from kivy import Config
Config.set('graphics', 'multisamples', '0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

class Tictactoe(AnchorLayout):
    pass   

class StatusBar(BoxLayout):
    pass

class Board(GridLayout):
    pass  
    
class Option(BoxLayout):
    pass

class TictactoeApp(App):
    def build(self):
        return Tictactoe()
    
if __name__ == "__main__":
    TictactoeApp().run()
