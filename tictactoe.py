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
from kivy.uix.image import Image

class Tictactoe(AnchorLayout):
    table = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    
    def tableError(self, i):
    # Check if select point isn't empty
        if(self.table[i] != ' '):
            print('ซ้ำ!!')
            return True
        else:
            return False

class StatusBar(BoxLayout):
    turn = NumericProperty(1)
    
    def on_turn(self, instance, value):
        player = self.checkPlayer()
        self.status_msg.text = player + ' Turn'
        
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
            if self.children[i].collide_point(touch.x, touch.y) and \
            not self.tictactoe.tableError(i):
                print(i+1)
                self.add(i)

    def add(self, i):
        if (self.status_bar.checkPlayer() == 'X'):
            mark = Image(source='X.png')
            self.tictactoe.table[i] = 'X'
        else:
            mark = Image(source='O.png')
            self.tictactoe.table[i] = 'O'
        self.children[i].add_widget(mark)
        self.status_bar.turn +=1

class Option(BoxLayout):
    def save(self, instance):
        file = open("savedata.txt", "w")
        data = ''
        for mark in self.parent.parent.table:
            data += mark
        file.write(data)
        file.close()
        print("Save" + data)

    def load(self, instance):
        file = open("savedata.txt", "r")
        data = file.readline()
        for i in range (0, len(data)):
            self.parent.parent.table[i] = data[i]
        file.close()
        print("Load" + str(self.parent.parent.table))

class TictactoeApp(App):
    def build(self):
        return Tictactoe()
    
if __name__ == "__main__":
    TictactoeApp().run()
