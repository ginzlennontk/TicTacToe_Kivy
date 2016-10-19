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
    def on_touch_down(self, touch):
        self.checkPos(touch)
        return super(Tictactoe, self).on_touch_down(touch)

    def checkPos(self,touch):
        for i in range (0,9):
            sizeX = self.width/6    # ความกว้างของช่อง
            sizeY = self.height/6   # ความยาวของช่อง
            x = (self.width/4) + ((i % 3)*sizeX)    # self.width/4 คือ ตำแหน่งซ้ายสุดของตาราง | i%3 เพื่อเช็คว่าอยู่ row ไหน
            y = (self.height/4) + ((i // 3)*sizeY)  # self.heigth/4 คือ ตำแหน่งล่างสุดของตาราง | i//3 เพื่อเช็คว่าอยู่ columm ไหน
            if(touch.x > x and touch.x < x+sizeX and touch.y > y and touch.y < y+sizeY):
                print(i+1)
        

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
