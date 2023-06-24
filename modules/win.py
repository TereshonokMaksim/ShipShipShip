import modules.data_base as data 
import pygame, os
pygame.font.init()
class Win_counter():
    def __init__(self):
        self.WIDTH = 200
        self.HEIGHT = 100
        self.X = 800
        self.Y = 0 
        self.COUNTER = [0,0]
    def win_blit(self,screen):
        # print("Я СЧЕТЧИК! Я СНОВА С ВАМИ!")
        font = pygame.font.SysFont("arial", size=40)
        image = pygame.image.load(os.path.abspath(f"images\\win\\win_counter.png"))
        image = pygame.transform.scale(image,(self.WIDTH,self.HEIGHT))
        screen.blit(image,(self.X,self.Y))
        player_count = font.render(str(self.COUNTER[0]),True,(0,0,0))
        enemy_count = font.render(str(self.COUNTER[1]),True,(0,0,0))
        screen.blit(player_count,(self.X + 45,self.Y + 40))
        screen.blit(enemy_count,(self.X + 145,self.Y + 40))
win_counter = Win_counter()
def win_check():
    
    player_ship_cells = 0
    player_bombed_cells = 0
    enemy_ship_cells = 0
    enemy_bombed_cells = 0
    for row in data.player_map:
        for cell in row:
            if cell.ITEM == "Ship":
                player_ship_cells += 1
            if cell.EFFECT == "explosion":
                player_bombed_cells += 1
    for row1 in data.enemy_map:
        for cell1 in row1:
            if cell1.ITEM == "Ship":
                enemy_ship_cells += 1
            if cell1.EFFECT == "explosion":
                enemy_bombed_cells += 1
    if player_ship_cells == player_bombed_cells and player_ship_cells != 0:
        if data.win:
            win_counter.COUNTER[1] += 1
        return "Enemy"  
    elif enemy_ship_cells == enemy_bombed_cells:
        if data.win:
            win_counter.COUNTER[0] += 1
        return "Player"
    else:
         return None
def blit_win(screen):
    winner = win_check()
    if winner != None:
        image = pygame.image.load(os.path.abspath(f"images\\win\\{winner}_sign.png"))
        image = pygame.transform.scale(image,(400,100))
        screen.blit(image,(300,100))
# def destroy_ship(map, ship):
#     def fill_area_in_bubbles(lenght, map, ship):
#         for cells in range(lenght + 2):
#             cell_edit = cells - 1
#             if ship.ANGLE == 270 and ship.CELL[0] + cell_edit < 10 and ship.CELL[0] - cell_edit > -1:
#                 if ship.CELL[1] - 1 > -1:
#                     map[ship.CELL[0] - cell_edit][ship.CELL[1] - 1].EFFECT = "cross"
#                 elif ship.CELL[0] + 1 < 10:
#                     map[ship.CELL[0] + cell_edit][ship.CELL[1] + 1].EFFECT = "cross"
#                 if map[ship.CELL[0] + cell_edit][ship.CELL[1]].EFFECT == 0:
#                     map[ship.CELL[0] + cell_edit][ship.CELL[1]].EFFECT = "cross"
#             elif ship.ANGLE == 180 and ship.CELL[0] + cell_edit > -1 and ship.CELL[1] + cell_edit < 10 and ship.CELL[1] - cell_edit > -1:
#                 if ship.CELL[0] - 1 > -1:
#                     map[ship.CELL[0] - 1][ship.CELL[1] + cell_edit].EFFECT = "cross"
#                 elif ship.CELL[0] + 1 < 10:
#                     map[ship.CELL[0] + 1][ship.CELL[1] + cell_edit].EFFECT = "cross"
#                 if map[ship.CELL[0]][ship.CELL[1] + cell_edit].EFFECT == 0:
#                     map[ship.CELL[0]][ship.CELL[1] + cell_edit].EFFECT = "cross"
#             elif ship.ANGLE == 90 and ship.CELL[0] + cell_edit > -1 and ship.CELL[0] + cell_edit < 10 and ship.CELL[0] - cell_edit > -1:
#                 if ship.CELL[1] - 1 > -1:
#                     map[ship.CELL[0] - cell_edit][ship.CELL[1] - 1].EFFECT = "cross"
#                 elif ship.CELL[1] + 1 < 10:
#                     map[ship.CELL[0] + cell_edit][ship.CELL[1] + 1].EFFECT = "cross"
#                 if map[ship.CELL[0] + cell_edit][ship.CELL[1]].EFFECT == 0:
#                     map[ship.CELL[0] + cell_edit][ship.CELL[1]].EFFECT = "cross"
#             elif ship.ANGLE == 0 and ship.CELL[0] + cell_edit > -1 and ship.CELL[1] + cell_edit < 10 and ship.CELL[1] - cell_edit > -1:
#                 if ship.CELL[0] - 1 > -1:
#                     map[ship.CELL[0] - 1][ship.CELL[1] + cell_edit].EFFECT = "cross"
#                 elif ship.CELL[0] + 1 < 10:
#                     map[ship.CELL[0] + 1][ship.CELL[1] + cell_edit].EFFECT = "cross"
#                 if map[ship.CELL[0]][ship.CELL[1] + cell_edit].EFFECT == 0:
#                     map[ship.CELL[0]][ship.CELL[1] + cell_edit].EFFECT = "cross"
#             return map
#     def check_ship(ship):
#         lenght = -2
#         if ship.TYPE == "Mini":
#             lenght = 1
#         elif ship.TYPE == "Normal":
#             lenght = 2
#         elif ship.TYPE == "Big":
#             lenght = 3
#         elif ship.TYPE == "Huge":
#             lenght = 4
#         cell_borders = [-1, lenght]
#         if ship.ANGLE == 0:
#             for cell_unedit in range(lenght):
#                 if 
                
                

        