'''
    Цей модуль відповідає за встановлення кораблей
    ігрока, а також все що з цим пов'язано
'''
# імпортування pygame 
import pygame 
# імпорт modules.data_base як data
import modules.data_base as data
# імпорт modules.ship як sh
import modules.ship as sh
# створюємо не установленого корабля с не уставленними координатами
data.unplaced_ship = sh.Ship(cell = [0,0,0], type = "Mini", side = "Player", angle = 0)
# перелік с усіма типами кораблів які будуть встановлені у майбутньому
ship_list = ["Mini","Mini","Mini","Mini","Normal","Normal","Normal","Big","Big","Huge"]
# поточний номер корабеля (указуються як індекс переліку ship_list)
current_ship = 1
# Створюємо функцію choose_ship
def choose_ship():
    global current_ship
    if current_ship < 11:
        # Створюємо перевірку,якщо змінна з об'єктом == "Mini" то 
        if data.unplaced_ship.TYPE == "Mini":
            # Створюємо змінну y_max зі значенням 70
            y_max = 70
        # Створюємо перевірку,якщо data.unplaced_ship.TYPE == "Normal" то
        elif data.unplaced_ship.TYPE == "Normal":
            # Створюємо змінну y_max 
            y_max = 120
        #Створюємо перевірку,якщо змінна з об'єктом == "Big" то 
        elif data.unplaced_ship.TYPE == "Big":
            # Створюємо y_max зі значенням 170
            y_max = 170 
        # Створюємо перевірку,якщо data.unplaced_ship.TYPE == "Huge":то
        elif data.unplaced_ship.TYPE == "Huge":
            # Створюємо y_max зі значенням 220 Створюємо змінну y_max зі значенням 220
            y_max = 220
        # Створюємо перевірку
        else:
            # Створюємо змінну y_max зі значенням 9
            # Створюємо змінну y_max зі значенням 9
            y_max = 9
        if data.unplaced_ship.TYPE   == "Mini":      
            lenght = 25
        elif data.unplaced_ship.TYPE == "Normal":    
            lenght = 75
        elif data.unplaced_ship.TYPE == "Big":       
            lenght = 125
        elif data.unplaced_ship.TYPE == "Huge":      
            lenght = 175
        data.unplaced_ship.WIDTH = lenght * 48 
    
        
    # print(pygame.mouse.get_pos())
    # область координат у якій відбувається реакція коли ми натискаємо на клітину
        if data.unplaced_ship.ANGLE == 0 or data.unplaced_ship.ANGLE == 180:
            if 10 < pygame.mouse.get_pos()[0] < y_max and 10 < pygame.mouse.get_pos()[1] < 70:
                # зміна  значення властивості на Hover
                data.unplaced_ship.STATE = "Hover"
        elif data.unplaced_ship.ANGLE == 90 or data.unplaced_ship.ANGLE == 270:
            if 10 < pygame.mouse.get_pos()[0] < 70 and 10 < pygame.mouse.get_pos()[1] < y_max:
                # зміна  значення властивості на Hover
                data.unplaced_ship.STATE = "Hover"
    # створення функції replace_shiр
def replace_ship():
    # створення умови якщо значення параметру STATE == Hover
    if data.unplaced_ship.STATE == "Hover":
        if data.unplaced_ship.TYPE   == "Mini":      
            lenght = 25
        elif data.unplaced_ship.TYPE == "Normal":    
            lenght = 75
        elif data.unplaced_ship.TYPE == "Big":       
            lenght = 125
        elif data.unplaced_ship.TYPE == "Huge":      
            lenght = 175
        if data.unplaced_ship.ANGLE == 270:
            print(270, end="GG")
            data.unplaced_ship.Y = pygame.mouse.get_pos()[1] - 25
            data.unplaced_ship.X = pygame.mouse.get_pos()[0] - 25
        elif data.unplaced_ship.ANGLE == 0:
            print(0)
            data.unplaced_ship.Y = pygame.mouse.get_pos()[1] - 25
            data.unplaced_ship.X = pygame.mouse.get_pos()[0] - 25
        elif data.unplaced_ship.ANGLE == 90:
            print(90)
            data.unplaced_ship.Y = pygame.mouse.get_pos()[1] - lenght
            data.unplaced_ship.X = pygame.mouse.get_pos()[0] - 25
        elif data.unplaced_ship.ANGLE == 180:
            print(180)
            data.unplaced_ship.Y = pygame.mouse.get_pos()[1] - 25
            data.unplaced_ship.X = pygame.mouse.get_pos()[0] - lenght
        print(lenght, data.unplaced_ship.ANGLE)
        # ми задаємо координату х нашому не виставленому кораблю на координату на х миші зменшеною шириною корабля яка поділена на 2
        
# Створюємо функцію check_cells
def check_cells():
    # Створюємо функцію check_cells_plus з параметром lenght
    def check_cells_plus(lenght):
        # Створюємо змінну list_cells зі значенням 0 
        list_cells = 0
        # Створюємо цикл 
        for value in range(lenght):
            # якщо кут повороту == 0 і клітка буде знаходитися корабель не знаходится за межами карти
            if data.unplaced_ship.ANGLE == 0 and data.unplaced_ship.CELL[1]+value<10:
                if data.player_map[data.unplaced_ship.CELL[0]][data.unplaced_ship.CELL[1]+value].ITEM == 0:
                    # збільшування list_cells на 1
                    list_cells += 1
                # якщо кут повороту == 90 і клітка буде знаходитися корабель не знаходится за межами карти
            elif data.unplaced_ship.ANGLE == 90 and data.unplaced_ship.CELL[0]-value>-1:
                if data.player_map[data.unplaced_ship.CELL[0]-value][data.unplaced_ship.CELL[1]].ITEM == 0:
                    # збільшування list_cells на 1
                    list_cells += 1
                # якщо кут повороту == 180 і клітка буде знаходитися корабель не знаходится за межами карти
            if data.unplaced_ship.ANGLE == 180 and data.unplaced_ship.CELL[1]-value>-1:
                if data.player_map[data.unplaced_ship.CELL[0]][data.unplaced_ship.CELL[1]-value].ITEM == 0:
                    # збільшування list_cells на 1
                    list_cells += 1
                # якщо кут повороту == 270 і клітка буде знаходитися корабель не знаходится за межами карти
            elif data.unplaced_ship.ANGLE == 270 and data.unplaced_ship.CELL[0]+value<10:
                if data.player_map[data.unplaced_ship.CELL[0]+value][data.unplaced_ship.CELL[1]].ITEM == 0:
                    # збільшування list_cells на 1
                    list_cells += 1
                # створюємо перевірку якщо list_cells == lenght то повертаємо значення True
        # print(f"Type: {data.unplaced_ship.TYPE}\nCorrect: {list_cells}/{lenght}\nAngle: {data.unplaced_ship.ANGLE}")
        if list_cells == lenght:       return True
        # якщо минула умова не виконю
        else:                          return False
        # 
    
    if len(data.unplaced_ship.CELL) == 2:
        if data.unplaced_ship.TYPE == "Mini":
            if data.player_map[data.unplaced_ship.CELL[0]][data.unplaced_ship.CELL[1]].ITEM == 0: return True 
            else: return False
        if data.unplaced_ship.TYPE == "Normal":
            return check_cells_plus(2)
        if data.unplaced_ship.TYPE == "Big":
            return check_cells_plus(3)
        if data.unplaced_ship.TYPE == "Huge":
            return check_cells_plus(4)

def place_busy_cells():
    def place_busy_cells_plus(lenght):
        for value in range(abs(lenght)+2):
            value_edit = value - 1
            if data.unplaced_ship.ANGLE == 270:
                if -1 < data.unplaced_ship.CELL[0] + value_edit < 10:
                    if data.unplaced_ship.CELL[1]+1 <= 9:
                        data.player_map[data.unplaced_ship.CELL[0] + value_edit][data.unplaced_ship.CELL[1] + 1].ITEM = "Busy"
                    if data.unplaced_ship.CELL[1]-1 > -1:
                        data.player_map[data.unplaced_ship.CELL[0] + value_edit][data.unplaced_ship.CELL[1] - 1].ITEM = "Busy"
                    data.player_map[data.unplaced_ship.CELL[0] + value_edit][data.unplaced_ship.CELL[1]    ].ITEM = "Busy"
            elif data.unplaced_ship.ANGLE == 180:
                if -1 < data.unplaced_ship.CELL[1] - value_edit < 10:
                    if data.unplaced_ship.CELL[0]+1 <= 9:
                        data.player_map[data.unplaced_ship.CELL[0] + 1][data.unplaced_ship.CELL[1] - value_edit].ITEM = "Busy"
                    if data.unplaced_ship.CELL[0]-1 > -1:
                        data.player_map[data.unplaced_ship.CELL[0] - 1][data.unplaced_ship.CELL[1] - value_edit].ITEM = "Busy"                
                    data.player_map[data.unplaced_ship.CELL[0]    ][data.unplaced_ship.CELL[1] - value_edit].ITEM = "Busy"
            if data.unplaced_ship.ANGLE == 90:
                if  -1 < data.unplaced_ship.CELL[0] - value_edit < 10:
                    if data.unplaced_ship.CELL[1]+1 <= 9:
                        data.player_map[data.unplaced_ship.CELL[0] - value_edit][data.unplaced_ship.CELL[1] + 1].ITEM = "Busy"
                    if data.unplaced_ship.CELL[1]-1 > -1:
                        data.player_map[data.unplaced_ship.CELL[0] - value_edit][data.unplaced_ship.CELL[1] - 1].ITEM = "Busy"
                    data.player_map[data.unplaced_ship.CELL[0] - value_edit][data.unplaced_ship.CELL[1]   ].ITEM = "Busy"
            elif data.unplaced_ship.ANGLE == 0:
                if -1 < data.unplaced_ship.CELL[1] + value_edit < 10:
                    if data.unplaced_ship.CELL[0]+1 <= 9:
                        data.player_map[data.unplaced_ship.CELL[0] + 1][data.unplaced_ship.CELL[1] + value_edit].ITEM = "Busy"
                    if data.unplaced_ship.CELL[0]-1 > -1:
                        data.player_map[data.unplaced_ship.CELL[0] - 1][data.unplaced_ship.CELL[1] + value_edit].ITEM = "Busy"
                    data.player_map[data.unplaced_ship.CELL[0]    ][data.unplaced_ship.CELL[1] + value_edit].ITEM = "Busy"
    if data.unplaced_ship.TYPE == "Mini":
        place_busy_cells_plus(1)
    if data.unplaced_ship.TYPE == "Normal":
        place_busy_cells_plus(2)
    if data.unplaced_ship.TYPE == "Big":
        place_busy_cells_plus(3)
    if data.unplaced_ship.TYPE == "Huge":
        place_busy_cells_plus(4)
def place_check():
    cell_num = [0,0]
    for row in data.player_map:
        # print(row)
        for cell in row:
            if cell_num == 99:
                continue
            elif cell.X < pygame.mouse.get_pos()[0] < cell.X + cell.WIDTH and cell.Y < pygame.mouse.get_pos()[1] < cell.Y + cell.HEIGHT:
                # print(f"Поставил в {cell_num}")
                # print(f"Координаты мыши: {pygame.mouse.get_pos()}, \n Координаты клетки: {cell.X}, {cell.Y}, \n Клетка: {cell_num}")
                data.unplaced_ship.CELL = cell_num
                cell_num = 99
            else:
                
                if cell_num[1] == 9:
                    cell_num[1] = 0
                    cell_num[0] += 1
                else:
                    cell_num[1] += 1
def ship_placement_done():
    global current_ship
    global ship_list
    if current_ship < 11:
        # print(f"Type: {data.unplaced_ship.TYPE} \nAngle: {data.unplaced_ship.ANGLE}")
        if data.unplaced_ship.TYPE   == "Mini":      lenght = 0 
        elif data.unplaced_ship.TYPE == "Normal":    lenght = 1
        elif data.unplaced_ship.TYPE == "Big":       lenght = 2
        elif data.unplaced_ship.TYPE == "Huge":      lenght = 3
        if data.unplaced_ship.ANGLE == 90:           data.unplaced_ship.CELL[0] -= lenght
        elif data.unplaced_ship.ANGLE == 180:        data.unplaced_ship.CELL[1] -= lenght 
        data.ships.append(data.unplaced_ship)
        data.ships[-1].cell_ship()
        if current_ship < 10:
            data.unplaced_ship = sh.Ship(cell = [0,0,0], type = ship_list[current_ship], side = "Player", angle = 0)
            lenght += 1
                # data.unplaced_ship.HEIGHT = lenght * 48 
            data.unplaced_ship.WIDTH = lenght * 48 + 48
            data.unplaced_ship.X = 10
            data.unplaced_ship.Y = 10
    current_ship += 1
    
def controls():  
    keys = pygame.key.get_pressed()
    if data.unplaced_ship.TYPE   == "Mini":      lenght = 1
    elif data.unplaced_ship.TYPE == "Normal":    lenght = 2
    elif data.unplaced_ship.TYPE == "Big":       lenght = 3
    elif data.unplaced_ship.TYPE == "Huge":      lenght = 4
    if keys[pygame.K_DOWN] == True:
        data.unplaced_ship.ANGLE = 90 
    if keys[pygame.K_LEFT] == True:
        data.unplaced_ship.ANGLE = 0
    if keys[pygame.K_UP] == True:
        data.unplaced_ship.ANGLE = 270
    if keys[pygame.K_RIGHT] == True:
        data.unplaced_ship.ANGLE = 180
    data.unplaced_ship.WIDTH = lenght * 48 
def placement_finish():
    data.unplaced_ship.STATE = "Normal"
    place_check()
    approval = check_cells()
    if approval:
        place_busy_cells()
        ship_placement_done()
    else:
        data.unplaced_ship.X = 10
        data.unplaced_ship.Y = 10
# def fill_ships(map):