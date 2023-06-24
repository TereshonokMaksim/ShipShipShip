import pygame, os
import modules.data_base as data
import modules.enemy as enemy
import modules.place_player_ships as pps
import modules.ship as sh
class Button ():
    def __init__(self,x = 0,y = 0,width = 0,height = 0):
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.STATE = "unpressed"
    def blit_button(self,screen):
        image = pygame.image.load(os.path.abspath(f"images\\buttons\\button_{self.STATE}.png"))
        image = pygame.transform.scale(image,(self.WIDTH,self.HEIGHT))
        screen.blit(image,(self.X,self.Y))
    def click_button(self, event):
        if event == "Click":
            self.STATE = "pressed"
        elif event == "Up":
            self.STATE = "unpressed"
            for row in data.player_map:
                for cell in row:
                    cell.ITEM = 0
                    cell.EFFECT = 0  
            data.ships = []
            enemy.place_enemy_ships()
            pps.current_ship = 1
            data.unplaced_ship = sh.Ship(cell = [0,0,0], type = "Mini", side = "Player", angle = 0)
            enemy.target = 0
            enemy.shoot = [0,0]
            

        print(self.STATE)