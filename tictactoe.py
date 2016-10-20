import kivy
kivy.require('1.9.0')
from kivy import Config
Config.set('graphics', 'multisamples', '0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty

class Tictactoe(AnchorLayout):
    pass

class StatusBar(BoxLayout):
    turn = NumericProperty(1)
    player = StringProperty('X')
    
    def on_turn(self, instance, value):
        self.player = self.checkPlayer()
        
    def checkPlayer(self):
        if (self.turn%2 == 0):
            return 'O'
        else:
            return 'X'

class Board(GridLayout):
    def on_touch_down(self, touch):
        self.checkPos(touch)
        return super(Board, self).on_touch_down(touch)

    def checkPos(self,touch):
        for i in range (0, len(self.children)):
            if self.children[i].collide_point(touch.x, touch.y):
                self.status_bar.turn +=1
                print(i+1)
    
class Option(BoxLayout):
    pass

class TictactoeApp(App):
    def build(self):
        return Tictactoe()
    
if __name__ == "__main__":
    TictactoeApp().run()
