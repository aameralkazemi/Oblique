import pygame as pg
from mainmenu import MainMenu

class TheGame():
    def __init__(self):
        """
        Initializing the window, flags, and keystrokes for The Game Class
        """
        pg.init()
        pg.display.set_caption('OBLIQUE by YOUSOF KAYAL')
        icon = pg.image.load("assets/icon.png")
        pg.display.set_icon(icon)
        self.running, self.start = True, False
        self.up_KEY, self.down_KEY, self.start_KEY, self.back_KEY = False, False, False, False

        self.display_WIDTH, self.display_HEIGHT = 1000, 800
        self.display = pg.Surface((self.display_WIDTH,self.display_HEIGHT))
        self.window = pg.display.set_mode(((self.display_WIDTH,self.display_HEIGHT)))
        self.black, self.white, self.magenta = (0,0,0), (255,255,255), (90,35,175)

        self.menu_font = 'assets/PoppkornRegular-MzKY.ttf'
        self.game_font = 'assets/PressStart2P-vaV7.ttf'
        
        self.current_menu = MainMenu(self)

    def loop(self):
        """
        The game loop, this is where the actual game lives.
        """        
        while self.start:
            self.listen_event()
            if self.start_KEY:
                self.running = False
                
            self.display.fill(self.black)
            self.render_text("Hello world HAHAHAHAAHAHAHA", 20 , self.display_WIDTH/2, self.display_HEIGHT/2)

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
                pg.quit()
                

            #tracking user input 
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.start_KEY = True
                if event.key == pg.K_ESCAPE:
                    self.back_KEY = True  
                if event.key == pg.K_DOWN:
                    self.down_KEY = True  
                if event.key == pg.K_UP:
                    self.up_KEY = True
                    
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
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface,text_rect)