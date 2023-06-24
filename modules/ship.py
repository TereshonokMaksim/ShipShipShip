'''
    Цей модуль потрібен для створення класса корабля
    ПК - Параметр Класса
'''
# імпортування pygame
import pygame, os 
# імпортування modules.data_base та перейменування як data
import modules.data_base as data
# створюємо класс Ship
class Ship():
    # Метод конструктор
    def __init__(self,cell = [0,0],type = None, side = None, angle = 0, state = "Live"):
        # Задаємо данні в метод конструктор 
        # ПК - параметр классу
        # Задаємо ПК CELL
        self.CELL = cell
        # Задаємо ПК WIDTH
        self.WIDTH = 50
        # Задаємо ПК HEIGHT
        self.HEIGHT = 50
        # Задаємо ПК ANGLE
        self.ANGLE = angle
        # Задаємо ПК TYPE
        self.TYPE = type
        self.STATE = None
        # Задаємо ПК SIDE
        self.SIDE = side
        # Задаємо ПК X
        self.X = 0
        # Задаємо ПК Y
        self.Y = 0
        self.STATE = state
        self.DESTROY = 0
    # Створюємо функцію cell_ship для автоматичного змінення предметів клітинок на відповідні кораблю
    def cell_ship(self):
        if self.TYPE == "Mini": lenght = 1
        if self.TYPE ==  "Normal": lenght = 2
        if self.TYPE == "Big": lenght = 3
        if self.TYPE == "Huge": lenght = 4
        for value in range(lenght):
            if self.SIDE == "Player": 
                self.X = data.player_map[self.CELL[0]][self.CELL[1]].X; self.Y = data.player_map[self.CELL[0]][self.CELL[1]].Y
                if self.ANGLE == 180:  data.player_map[self.CELL[0]][self.CELL[1] + value].ITEM = "Ship"
                elif self.ANGLE == 90:  data.player_map[self.CELL[0] + value][self.CELL[1]].ITEM = "Ship"
                elif self.ANGLE == 0:  data.player_map[self.CELL[0]][self.CELL[1] + value].ITEM = "Ship"
                elif self.ANGLE == 270:  data.player_map[self.CELL[0] + value][self.CELL[1]].ITEM = "Ship"
                # print(self.CELL)
                
            if self.SIDE == "Enemy": 
                self.X = data.enemy_map[self.CELL[0]][self.CELL[1]].X; self.Y = data.enemy_map[self.CELL[0]][self.CELL[1]].Y
                if self.ANGLE == 180:  data.enemy_map[self.CELL[0]][self.CELL[1] - value].ITEM = "Ship"
                elif self.ANGLE == 90:  data.enemy_map[self.CELL[0] - value][self.CELL[1]].ITEM = "Ship"
                elif self.ANGLE == 0:  data.enemy_map[self.CELL[0]][self.CELL[1] + value].ITEM = "Ship"
                elif self.ANGLE == 270:  data.enemy_map[self.CELL[0] + value][self.CELL[1]].ITEM = "Ship"
        self.WIDTH = lenght * 48

    # def destroy_new_cell(self):
    #     if self.TYPE == "Mini": lenght = 1
    #     if self.TYPE ==  "Normal": lenght = 2
    #     if self.TYPE == "Big": lenght = 3
    #     if self.TYPE == "Huge": lenght = 4
    #     self.DESTROY += 1
    #     if self.DESTROY == lenght:
    #         self.STATE = "Death"
            

    # функцию для отображения кораблей
    def blit_ship(self,screen):
        # Завантажуємо картинку та повертаємо її на кількість градусів, яка указана в ПК "ANGLE"
        image = pygame.image.load(os.path.join(os.path.abspath(f"images\\ship\\{self.TYPE}_ship.png")))
        # Змінюємо розміри картинки на задану ширину (ПК WIDTH) та висоту (ПК HEIGHT)
        image = pygame.transform.scale(image,(self.WIDTH,self.HEIGHT))
        image = pygame.transform.rotate(image, self.ANGLE)
        # Показуємо картинку на екрані, який передаємо
        screen.blit(image,(self.X,self.Y))
        # print("я есть!!!")
        # print(f"где я: {self.X}, {self.Y}")