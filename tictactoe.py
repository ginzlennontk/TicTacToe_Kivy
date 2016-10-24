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
from kivy.graphics import Line, Color
from kivy.graphics import *

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
        self.tictactoe.table[i] = self.status_bar.checkPlayer()
        self.check_win()
        self.show_table()
        self.status_bar.turn +=1
        
    def check_win(self):
        tb = self.tictactoe.table
        for i in range (3):
            if (tb[i*3] == tb[(i*3)+1] == tb[(i*3)+2] != ' '):
                print(self.status_bar.checkPlayer())
                with self.canvas:
                    Color(1,1,0,1)
                    self.line = Line(points = (self.children[i*3].center_x,
                                               self.children[i*3].center_y,
                                               self.children[i*3+2].center_x,
                                               self.children[i*3+2].center_y),
                                     width = 5, group = 'line')
            elif (tb[i] == tb[i+3] == tb[i+6] != ' '):
                print(self.status_bar.checkPlayer())
                with self.canvas:
                    Color(1,1,0,1)
                    self.line = Line(points = (self.children[i].center_x,
                                               self.children[i].center_y,
                                               self.children[i+6].center_x,
                                               self.children[i+6].center_y),
                                     width = 5, group = 'line')
        if (tb[0] == tb[4] == tb[8] != ' '):
            print(self.status_bar.checkPlayer())
            with self.canvas:
                    Color(1,1,0,1)
                    self.line = Line(points = (self.children[0].center_x,
                                               self.children[0].center_y,
                                               self.children[8].center_x,
                                               self.children[8].center_y),
                                     width = 5, group = 'line')
        if (tb[2] == tb[4] == tb[6] != ' '):
            print(self.status_bar.checkPlayer())
            with self.canvas:
                    Color(1,1,0,1)
                    self.line = Line(points = (self.children[2].center_x,
                                               self.children[2].center_y,
                                               self.children[6].center_x,
                                               self.children[6].center_y),
                                     width = 5, group = 'line')
    
    def clear(self):
        for child in self.children:
            if(len(child.children) > 0):
                child.remove_widget(child.children[0])

    def show_table(self):
        self.clear()
        for i in range (len(self.tictactoe.table)):
            if(self.tictactoe.table[i] == 'X'):
                mark = Image(source='X.png')
            elif(self.tictactoe.table[i] == 'O'):
                mark = Image(source='O.png')
            else:
                mark = Image(source='Blank.png')
            self.children[i].add_widget(mark)

class Option(BoxLayout):
    def save(self, instance):
        file = open("savedata.txt", "w")
        data = ''
        for mark in self.parent.parent.table:
            data += mark
        file.write(data)
        file.close()
        print("Save" + data)
        self.board.show_table()

    def load(self, instance):
        self.board.canvas.remove_group('line')
        file = open("savedata.txt", "r")
        data = file.readline()
        turn_counter = 0
        for i in range (0, len(data)):
            self.parent.parent.table[i] = data[i]
            if(data[i] != ' '):
                turn_counter +=1
        file.close()
        print("Load" + str(self.parent.parent.table))
        self.board.show_table()
        self.board.check_win()
        self.status_bar.turn = turn_counter + 1

    def restart(self, instance, value):
        self.tictactoe.table = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.board.clear()
        self.board.canvas.remove_group('line')
        self.status_bar.turn = 1
        self.board.show_table()

class TictactoeApp(App):
    def build(self):
        return Tictactoe()
    
if __name__ == "__main__":
    TictactoeApp().run()
