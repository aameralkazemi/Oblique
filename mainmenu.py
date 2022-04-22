import pygame as pg

class MainMenu():
    def __init__(self,game):
        """
        Initializing Main Menu Class

        Args:
            game (file): Contains "TheGame" Class, inheriting the contents
        """
        self.game = game

        #initializing run_display flag, and initializing selection to "Start"
        self.run_display = True
        self.selection = "Start"

        self.startx, self.starty = self.game.mid_WIDTH, self.game.mid_HEIGHT + 50
        self.creditsx, self.creditsy = self.game.mid_WIDTH, self.game.mid_HEIGHT + 95
        self.exitx, self.exity = self.game.mid_WIDTH, self.game.mid_HEIGHT + 135

        #initializing container for cursor, with offset 150 points to the left 
        self.cursor_rect = pg.Rect(0,0,45,45)
        self.offset = - 150
        #Calibrating cursor to selection -> "Start"
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        
    
    def blit_screen(self):
        self.game.window.blit(self.game.display,(0,0))
        pg.display.update()
        self.game.reset_key()

    def display(self):
        self.run_display = True
        while self.run_display:
            self.game.listen_event()
            self.listen_input()
            self.game.display.fill(self.game.black)

            self.game.render_text("Oblique", 200, self.game.menu_font, self.game.white, self.game.mid_WIDTH, self.game.mid_HEIGHT-100)
            self.game.render_text("Start Game", 60, self.game.menu_font, self.game.white, self.startx, self.starty)
            self.game.render_text("Credits", 60, self.game.menu_font, self.game.white, self.creditsx, self.creditsy)
            self.game.render_text("Exit", 60, self.game.menu_font, self.game.white, self.exitx, self.exity)

            #cursor creation using the create text method
            self.game.render_text('O', 40, self.game.menu_font, self.game.magenta, self.cursor_rect.x, self.cursor_rect.y)
            self.blit_screen()
    
    def move_cursor(self):
        """
        Funtion that moves cursor in accordance to 'up' and 'down' inputs
        """
        if self.game.down_KEY:
            if self.selection == "Start":
                self.cursor_rect.midtop = (self.creditsx + self.offset+50, self.creditsy)
                self.selection = "Credits"
            elif self.selection == "Credits":
                self.cursor_rect.midtop = (self.exitx + self.offset+90, self.exity)
                self.selection = "Exit"
            elif self.selection == "Exit":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.selection = "Start"

        if self.game.up_KEY:
            if self.selection == "Start":
                self.cursor_rect.midtop = (self.exitx + self.offset+90, self.exity)
                self.selection = "Exit"
            elif self.selection == "Credits":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.selection = "Start"
            elif self.selection == "Exit":
                self.cursor_rect.midtop = (self.creditsx + self.offset+50, self.creditsy)
                self.selection = "Credits"
        
    
    def listen_input(self):
        """
        Listens for user input of "start" button. Depending on self.selection value, opens corresponding menu.
        """
        self.move_cursor()
        if self.game.start_KEY:
            if self.selection == "Start":
                print(self.game.start)
                self.game.start = True
            elif self.selection == "Credits":
                self.game.current_menu = self.game.credits
            elif self.selection == "Exit":
                self.game.running, self.game.start = False, False
            self.run_display= False
                
class Credits():
    def __init__(self, game):
        self.game = game
        self.run_display = True

    def display(self):
        self.run_display = True
        while self.run_display:
            self.game.listen_event()
            if self.game.back_KEY or self.game.start_KEY:
                self.game.current_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.black)
            self.game.render_text('Credits', 100, self.game.menu_font, self.game.white, self.game.mid_WIDTH, self.game.mid_HEIGHT - 20)
            self.game.render_text('By Yousof Kayal', 50, self.game.menu_font, self.game.magenta, self.game.mid_WIDTH, self.game.mid_HEIGHT +40)
            self.game.window.blit(self.game.display,(0,0))
            pg.display.update()
            self.game.reset_key()

