# Імпортуємо модуль pygame 
import pygame, os
# Створюється клас Cell
class Cell():
    # Створюємо функцію метод - конструктор 
    def __init__(self,x=0,y=0,state=0,item=0):
        # Створюємо змінну з назвою X,передаємо значення x
        self.X = x
        # Створюємо змінну з назвою Y,передаємо значення y
        self.Y = y
        # Створюємо змінну з назвою STATE,передаємо значення state
        self.STATE = state 
        # Створюємо змінну з назвою ITEM,передаємо значення item
        self.ITEM = item
        self.EFFECT = 0
        # Створюємо змінну з назвою WIDTH,передаємо значення 48
        self.WIDTH = 50
        # Створюємо змінну з назвою HEIGHT,передаємо значення 48
        self.HEIGHT = 50
    # Створюємо функцію blit_cell з параметрами self,screen
    def blit_cell(self,screen):
        # Створюємо перевірку 
        # Якщо self.STATE == "normal" то:
        if self.STATE == "normal":
            '''Малюємо прямокутник.Передаємо туди параметри : параметри surface,color,rect
            В surface передаємо параметр screen,прикріпляємо прямокутник до screen
            В color передаємо значення(0,166,199),тобто (червоний - 0,зелений  - 166,синій - 199)
            В rect передаємо Х,У,WIDTH,HEIGHT'''
            pygame.draw.rect(surface=screen,color=(0, 166, 199), rect=(self.X,self.Y,self.WIDTH,self.HEIGHT))
            '''Малюємо прямокутник.Передаємо туди параметри : параметри surface,color,rect
            В surface передаємо параметр screen,прикріпляємо прямокутник до screen
            В color передаємо значення(0,0,0),тобто (червоний - 0,зелений  - 0,синій - 0)
            В rect передаємо Х,У,WIDTH,HEIGHT'''
            pygame.draw.rect(surface=screen,color=(0, 0, 0), rect=(self.X,self.Y,self.WIDTH,self.HEIGHT),width=3)
        # Якщо self.STATE == "hover"то :
        elif self.STATE == "hover":
            ''' Малюємо прямокутник.Передаємо туди параметри : параметри surface,color,rect
            В surface передаємо параметр screen,прикріпляємо прямокутник до screen
            В color передаємо значення(0,213,255),тобто (червоний - 0,зелений  - 213,синій - 255)
            В rect передаємо Х,У,WIDTH,HEIGHT'''
            pygame.draw.rect(surface=screen,color=(0, 213, 255), rect=(self.X,self.Y,self.WIDTH,self.HEIGHT))
            '''Малюємо прямокутник.Передаємо туди параметри : параметри surface,color,rect
            В surface передаємо параметр screen,прикріпляємо прямокутник до screen
            В color передаємо значення(0,0,0),тобто (червоний - 0,зелений  - 0,синій - 0)
            В rect передаємо Х,У,WIDTH,HEIGHT'''
            pygame.draw.rect(surface=screen,color=(0, 0, 0), rect=(self.X,self.Y,self.WIDTH,self.HEIGHT),width=2)
        # Якщо self.STATE == "pressed"то :
        elif self.STATE == "pressed":
            '''Малюємо прямокутник.Передаємо туди параметри : параметри surface,color,rect
            В surface передаємо параметр screen,прикріпляємо прямокутник до screen
            В color передаємо значення(0,126,150),тобто (червоний - 0,зелений  - 126,синій - 150)
            В rect передаємо Х,У,WIDTH,HEIGHT'''
            pygame.draw.rect(surface=screen,color=(0, 126, 150), rect=(self.X,self.Y,self.WIDTH,self.HEIGHT))
            '''Малюємо прямокутник.Передаємо туди параметри : параметри surface,color,rect
            В surface передаємо параметр screen,прикріпляємо прямокутник до screen
            В color передаємо значення(0,0,0),тобто (червоний - 0,зелений  - 0,синій - 0)
            В rect передаємо Х,У,WIDTH,HEIGHT'''
            pygame.draw.rect(surface=screen,color=(0, 0, 0), rect=(self.X,self.Y,self.WIDTH,self.HEIGHT),width=4)
            
    def effect_blit(self,screen):
        if self.EFFECT != 0:
            image = pygame.image.load(os.path.abspath(f"images\\{self.EFFECT}.png"))
            image = pygame.transform.scale(image,(self.WIDTH,self.HEIGHT))
            screen.blit(image,(self.X,self.Y))
            