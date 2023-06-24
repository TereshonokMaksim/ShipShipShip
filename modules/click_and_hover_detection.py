# Імпортуємо модуль pygame 
import pygame
# Імпортуємо data_base
import modules.data_base as data
# Створюєм функцюю click_hover_detection
def click_hover_detection(event):
    #Створюємо цикл for і передаєм значення в row
    for row in range(10):
        #Створюємо цикл фор та передаєм значення в cell 
        for cell in data.enemy_map[row]:
            #Створюєм умова якщо плитка дорівнює "hover"
            if cell.STATE == "hover":
                #стан клітинки змінюємо на "normal"
                cell.STATE = "normal"
            # event = pygame.event.get()
            # умова яка перевіряє натиснуто на кнопку по Х
            if cell.X < pygame.mouse.get_pos()[0] < cell.X + 48: 
                # друга умова яка перевіряє натиснуто на кнопку по У
                if cell.Y < pygame.mouse.get_pos()[1] < cell.Y + 48:
                    # перевірка чи натиснута кнопка миші
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # умова якщо вже натиснута кнопка миші 
                        if cell.STATE != "pressed" and cell.EFFECT == 0:
                            # Змінюємо стан клітки на "pressed" (тобто натиснута)
                            cell.STATE = "pressed"
                    # перевірка якщо відпущена клавіша миші
                    elif event.type == pygame.MOUSEBUTTONUP:
                        # Перевіряє, чи є стан клітки "pressed" (тобто натиснута)
                        if cell.STATE == "pressed":
                            # Змінюємо стан на "normal" (тобто звичайний)
                            cell.STATE = "normal"
                            if cell.EFFECT == 0:
                                
                                
                                # Змінюємо предмет клітки на хрестик
                                
                                if cell.ITEM == "Ship":
                                    # print("Boom")
                                    cell.EFFECT = "explosion"
                                    return False                            
                                else:
                                    # print("Nope")
                                    cell.EFFECT = "cross"
                                    return True                   
                    # Перевіряє, чи є предмет клітки відсутній
                    elif cell.EFFECT == 0:
                        # Змінюємо стан клітки на "hover"
                        cell.STATE = "hover"