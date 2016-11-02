import kivy
from kivy.uix.relativelayout import RelativeLayout
kivy.require('1.9.0')
from kivy import Config
Config.set('graphics', 'multisamples', '0')
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from kivy.uix.image import Image
from kivy.graphics import Line, Color
from kivy.graphics import *
from kivy.core.window import Window

class Tictactoe(AnchorLayout):
    table = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']               # array for storage data
    
    def tableError(self, i):
    # Check if select point isn't empty
        if(self.table[i] != ' '):
            print('ซ้ำ!!')
            return True
        else:
            return False

    def checkWin(self):
        for x in range(3):
            if(self.table[x] == self.table[x+3] == self.table[x+6] != " "):
                self.board.show_where_win(x, x+6)
                return True						# If true return current player win
            
            elif(self.table[3*x] == self.table[(3*x)+1] == self.table[(3*x)+2] != " "):
                self.board.show_where_win(3*x, (3*x)+2)
                return True						# If true return current player win
            
            elif(self.table[8] == self.table[4] == self.table[0] != " "):
                self.board.show_where_win(0, 8)
                return True						# If true return current player win
            
            elif(self.table[6] == self.table[4] == self.table[2] != " "):
                self.board.show_where_win(2, 6)
                return True						# If true return cuurent player win
        else:								# If none of this is true
            return False						# Return false nobody win keep playing or draw

    def checkDraw(self):						# Check draw
        for x in range(9):
            if self.table[x] == " ":		# If not then blank = 0
                return False
        return True
class Again(RelativeLayout):
     Yes = ObjectProperty(None)
     No = ObjectProperty(None)

class StatusBar(BoxLayout):
    turn = NumericProperty(1)
    countX = NumericProperty(0)
    countO = NumericProperty(0)
    
    def on_turn(self, instance, value):                     #change current player 
        player = self.checkPlayer()
        self.status_msg.text = player + ' Turn'
        
    def checkPlayer(self):                                  #check currnet player
        if (self.turn%2 == 0):
            return 'O'
        else:
            return 'X'

    '''def show_error(self):
        self.status_msg.text = 'Duplicate!!!'''
    def dismiss_popup(self):
        self._popup.dismiss()
   
    def show_win(self):
        player = self.checkPlayer()
        self.status_msg.text = player + ' Win!'
        self.Again()
    def Again(self):
        content = Again(No=self.dismiss_popup,Yes=self.countScore)
        self._popup = Popup(title='Play Again?', content=content, auto_dismiss=False, 
                            size_hint=(None, None), size=(500,150),
                            pos_hint={'x': .2 , 
                            'y':.0 })
        self._popup.open()
    def countScore(self):
        player = self.checkPlayer()
        self._popup.dismiss()
        self.tictactoe.table = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.board.clear()
        self.board.canvas.remove_group('line')
        self.turn = 1
        self.board.show_table()
        if player == 'X':
            self.countX += 1
        else:
            self.countO += 1
    def reDraw(self):
        self._popup.dismiss()
        self.tictactoe.table = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.board.clear()
        self.board.canvas.remove_group('line')
        self.turn = 1
        self.board.show_table()
    def DrawAgain(self):
        content = Again(No=self.dismiss_popup,Yes=self.reDraw)
        self._popup = Popup(title='Play Again?', content=content, auto_dismiss=False, 
                            size_hint=(None, None), size=(500,150),
                            pos_hint={'x': .2 , 'y':.0})
        self._popup.open()
    def show_draw(self):
        self.status_msg.text = 'DRAW'
        self.DrawAgain()

class Board(GridLayout):
    def on_touch_down(self, touch):
        self.checkPos(touch)
        return super(Board, self).on_touch_down(touch)

    def checkPos(self,touch):
        for i in range (0, len(self.children)):
            if self.children[i].collide_point(touch.x, touch.y) and \
            not self.tictactoe.tableError(i) and not self.tictactoe.checkWin():
                print(i+1)
                self.add(i)

    def add(self, i):
        self.tictactoe.table[i] = self.status_bar.checkPlayer()
        self.show_table()
        if(self.tictactoe.checkWin()):
            self.status_bar.show_win()		# Tell that O win
        elif(self.tictactoe.checkDraw()):
            self.status_bar.show_draw()
        else:
            self.status_bar.turn +=1
        
    def show_where_win(self, x1, x2):
            with self.canvas:
                    Color(1,1,0,1)
                    self.line = Line(points = (self.children[x1].center_x,
                                               self.children[x1].center_y,
                                               self.children[x2].center_x,
                                               self.children[x2].center_y),
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
        for mark in self.tictactoe.table:
            data += mark
        file.write(data)
        file.write(str(self.status_bar.countX))
        file.write(str(self.status_bar.countO))
        file.close()
        print("Save" + data)
        self.board.show_table()
        self.saved_message()
        
    def saved_message(self):
        box = BoxLayout()
        box.add_widget(Label(text='Your game has been saved.'))
        popup = Popup(title='Message', content=box, size_hint=(None, None), size=(300, 300))
        popup.open()
    
    def load_message(self):
        box = BoxLayout()
        box.add_widget(Label(text='Load Complete.'))
        popup = Popup(title='Message', content=box, size_hint=(None, None), size=(300, 300))
        popup.open()
        
    def load(self, instance):
        self.board.canvas.remove_group('line')
        file = open("savedata.txt", "r")
        data = file.readline()
        self.status_bar.turn = 0
        for i in range (0, 11):
            if(data[i] in ('X', 'O')):
                self.tictactoe.table[i] = data[i]
                self.status_bar.turn +=1
            elif i == 9:
                self.status_bar.countX = int(data[i])
                print(data[i])
            elif i == 10:
                self.status_bar.countO = int(data[i])
                print(data[i])
            elif i < 10 and data[i] == ' ':
                self.tictactoe.table[i] = ' '
        file.close()
        print("Load" + str(self.tictactoe.table))
        self.board.show_table()
        self.load_message()
        if(self.tictactoe.checkWin()):
            self.status_bar.show_win()		# Tell that O or X win
        elif(self.tictactoe.checkDraw()):
            self.status_bar.show_draw()
        else:
            self.status_bar.turn += 1

    def restart(self, instance, value):
        self.tictactoe.table = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.board.clear()
        self.board.canvas.remove_group('line')
        self.status_bar.turn = 1
        self.board.show_table()
        self.status_bar.countX = 0
        self.status_bar.countO = 0

class TictactoeApp(App):
    def build(self):
        return Tictactoe()
    
if __name__ == "__main__":
    TictactoeApp().run()
