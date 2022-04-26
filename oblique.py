import pygame as pg
from mainmenu import MainMenu, Credits
import time

class TheGame():
    def __init__(self):
        """
        Initializing the window, flags, the clock, and keystrokes for The Game Class
        """
        pg.init()
        pg.display.set_caption('OBLIQUE by YOUSOF KAYAL')
        icon = pg.image.load("assets/icon.png")
        pg.display.set_icon(icon)
        self.running, self.start = True, False
        self.up_KEY, self.down_KEY, self.start_KEY, self.back_KEY = False, False, False, False

        self.display_WIDTH, self.display_HEIGHT = 1280, 720
        self.mid_WIDTH, self.mid_HEIGHT = self.display_WIDTH/2, self.display_HEIGHT/2

        self.display = pg.Surface((self.display_WIDTH,self.display_HEIGHT))
        self.window = pg.display.set_mode(((self.display_WIDTH,self.display_HEIGHT)))
        self.black, self.white, self.magenta = (0,0,0), (255,255,255), (90,35,175)

        self.user_text = ''
        self.cursor = 0
        self.next_update= 0
        
        
        self.menu_font = 'assets/PoppkornRegular-MzKY.ttf'
        self.game_font = 'assets/PressStart2P-vaV7.ttf'
        self.dg_font = pg.font.Font(self.game_font, 20)
        self.dg_image   = self.dg_font.render( '*', True, self.black)
        
        
        self.main_menu = MainMenu(self)
        self.credits = Credits(self)
        self.current_menu = MainMenu(self)


    def main_loop(self):
        """
        The game loop, this is where the actual game lives.
        """
        while self.start:

      

            self.listen_event()

            if self.back_KEY:
                self.start = False
                self.user_text = ''
                self.dg_image.fill(self.black) 
            self.listen_event()
            self.display.fill(self.black)
            
            self.render_text(self.user_text, 15 ,self.game_font, self.white, self.mid_WIDTH-200, self.mid_HEIGHT+200)

            self.counter  = 0
            
            
            if self.user_text == "":
                self.render_text("press s to start the game", 15, self.game_font, self.white, 200, 100)
                self.counter = 0


            if self.user_text == "s":
                self.render_text("Welcome to Oblique !!", 15, self.game_font, self.white, 200, 100)
                self.render_text("An adventure based or whatever", 15, self.game_font, self.white, 250, 120)
                self.render_text("Press Y to Continue", 15, self.game_font, self.white, 250, 140)
                self.counter = 1

            if self.user_text == "sy" or self.user_text == "y" :
                self.render_text("Level 1 Please enter you name", 15, self.game_font, self.white, 200, 100)
                self.render_text("welcome Starnger to the land of the oblique and fuck you", 15, self.game_font, self.white, 250, 120)
                self.render_text("Press N to continue", 15, self.game_font, self.white, 250, 140)
                self.counter = 2
                self.user_text = "y"
      
            if self.user_text == "yn" or self.user_text == "n":
                self.render_text("Level 1 Please enter you name", 15, self.game_font, self.white, 200, 100)
                self.render_text("welcome to level 1", 15, self.game_font, self.white, 250, 120)
                self.counter = 3
                self.user_text = "n"
           
        
                

              
                
            

            self.window.blit(self.display,(0,0))
            pg.display.update()

            self.reset_key()

    def listen_event(self):
        """
        Function that is checking for user inputs
        """
        for event in pg.event.get():
            #exit game through "x" button
            if event.type == pg.QUIT:
                self.running, self.start = False, False
                self.current_menu.run_display= False
                
            #tracking user input for menu traversal 
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.start_KEY = True
                elif event.key == pg.K_ESCAPE:
                    self.back_KEY = True
                elif event.key == pg.K_DOWN:
                    self.down_KEY = True
                elif event.key == pg.K_UP:
                    self.up_KEY = True
                elif event.key == pg.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                else:
                    self.user_text += event.unicode
                    
                    
    def reset_key(self):
        """
        Reset user key presses
        """        
        self.start_KEY, self.back_KEY, self.down_KEY, self.up_KEY = False, False, False, False



    def render_text(self, text, size, font, color, x, y):
        """
        Rendering text in chosen font

        Args:
            text (String): The text that is being rendered
            size (Int): How large the text is
            font (String): What font to render
            color(Int): The color value for the rendered text
            x, y (Int): Where the text is located on the screen  
        """
        chosenfont = pg.font.Font(font,size)
        text_surface = chosenfont.render(text, True, color)
        render_rect = text_surface.get_rect()
        render_rect.center = (x, y)
        self.display.blit(text_surface,render_rect)


"""
Attributing "TheGame" class to a variable (ob) and the program loop
"""
ob = TheGame() 
while ob.running:
    ob.current_menu.display()
    ob.main_loop()
    