import pygame
# import modules.data_base as data 
# Імпортуємо модуль random
import random
import modules.data_base as data 
import modules.ship as sh
# Створюємо функцію place_enemy_ships
shoot = [0,0]
target = 0
sides = [[-1, 0],[0, -1],  [0, 1], [1, 0]]
line = 0
line_lenght = 0
end_of_line = False
side = 0
repeat = 0
line_ready = 0
def place_enemy_ships():
    # Створюємо перелік з назвою ships_list1
    # Створюємо перелік ships з значеннями "Huge","Big","Big","Normal",
    # "Normal","Normal","Mini","Mini","Mini","Mini"
    for row in range(len(data.enemy_map)):
        for cell in data.enemy_map[row]:
            cell.ITEM = 0 
            cell.EFFECT = 0
            
    ships = ["Huge","Big","Big","Normal",
    "Normal","Normal","Mini","Mini","Mini","Mini"]
    unplaced_ship = sh.Ship(cell = [0,0], type = "Mini", side = "Enemy", angle = 0)
    # Створюємо цикл for,який генерує кораблі 
    def check_cells(ship):
    # Створюємо функцію check_cells_plus з параметром lenght
        def check_cells_plus(lenght,unplaced_ship):
            # Створюємо змінну list_cells зі значенням 0 
            list_cells = 0
            # Створюємо цикл for 
            for value in range(lenght):
                # якщо кут повороту == 0 і клітка буде знаходитися корабель не знаходится за межами карти
                if unplaced_ship.ANGLE == 0 and unplaced_ship.CELL[1]+value<10:
                    if data.enemy_map[unplaced_ship.CELL[0]][unplaced_ship.CELL[1]+value].ITEM == 0:
                        # збільшування list_cells на 1
                        list_cells += 1
                    # якщо кут повороту == 90 і клітка буде знаходитися корабель не знаходится за межами карти
                elif unplaced_ship.ANGLE == 90 and unplaced_ship.CELL[0]-value>-1:
                    if data.enemy_map[unplaced_ship.CELL[0]-value][unplaced_ship.CELL[1]].ITEM == 0:
                        # збільшування list_cells на 1
                        list_cells += 1
                    # якщо кут повороту == 180 і клітка буде знаходитися корабель не знаходится за межами карти
                if unplaced_ship.ANGLE == 180 and unplaced_ship.CELL[1]-value>-1:
                    if data.enemy_map[unplaced_ship.CELL[0]][unplaced_ship.CELL[1]-value].ITEM == 0:
                        # збільшування list_cells на 1
                        list_cells += 1
                    # якщо кут повороту == 270 і клітка буде знаходитися корабель не знаходится за межами карти
                elif unplaced_ship.ANGLE == 270 and unplaced_ship.CELL[0]+value<10:
                    if data.enemy_map[unplaced_ship.CELL[0]+value][unplaced_ship.CELL[1]].ITEM == 0:
                        # збільшування list_cells на 1
                        list_cells += 1
                    # створюємо перевірку якщо list_cells == lenght то повертаємо значення True
            print(f"Type: {ship.TYPE}\nCorrect: {list_cells}/{lenght}\nAngle: {ship.ANGLE}")
            return list_cells == lenght
            # 
        if len(unplaced_ship.CELL) == 2:
            if unplaced_ship.TYPE == "Mini":
                return check_cells_plus(1,ship)
            if unplaced_ship.TYPE == "Normal":
                return check_cells_plus(2,ship)
            if unplaced_ship.TYPE == "Big":
                return check_cells_plus(3,ship)
            if unplaced_ship.TYPE == "Huge":
                return check_cells_plus(4,ship)
    def place_busy_cells(ship):
        def place_busy_cells_plus(lenght,unplaced_ship):
            for value in range(abs(lenght)+2):
                value_edit = value - 1
                if unplaced_ship.ANGLE == 270:
                    if unplaced_ship.CELL[0] + value_edit >= 0 and unplaced_ship.CELL[0] + value_edit < 10 and unplaced_ship.CELL[0] - value_edit > -1 and unplaced_ship.CELL[0] - value_edit < 10:
                        if unplaced_ship.CELL[1]+1 < 10:
                            data.enemy_map[unplaced_ship.CELL[0] + value_edit][unplaced_ship.CELL[1] + 1].ITEM = "Busy"
                        if unplaced_ship.CELL[1]-1 > -1:
                            data.enemy_map[unplaced_ship.CELL[0] + value_edit][unplaced_ship.CELL[1] - 1].ITEM = "Busy"
                        data.enemy_map[unplaced_ship.CELL[0] + value_edit][unplaced_ship.CELL[1]    ].ITEM = "Busy"
                elif unplaced_ship.ANGLE == 180:
                    if unplaced_ship.CELL[1] + value_edit < 10 and unplaced_ship.CELL[1] - value_edit > -1 and unplaced_ship.CELL[1] - value_edit < 10 and unplaced_ship.CELL[1] + value_edit > -1:
                        if unplaced_ship.CELL[0]+1 < 10:
                            data.enemy_map[unplaced_ship.CELL[0] + 1][unplaced_ship.CELL[1] - value_edit].ITEM = "Busy"
                        if unplaced_ship.CELL[0]-1 > -1:
                            data.enemy_map[unplaced_ship.CELL[0] - 1][unplaced_ship.CELL[1] - value_edit].ITEM = "Busy"                
                        data.enemy_map[unplaced_ship.CELL[0]    ][unplaced_ship.CELL[1] - value_edit].ITEM = "Busy"
                if unplaced_ship.ANGLE == 90:
                    if unplaced_ship.CELL[0] + value_edit < 10 and unplaced_ship.CELL[0] - value_edit > -1 and unplaced_ship.CELL[0] - value_edit < 10 and unplaced_ship.CELL[0] + value_edit > -1:
                        if unplaced_ship.CELL[1]+1 < 10:
                            data.enemy_map[unplaced_ship.CELL[0] - value_edit][unplaced_ship.CELL[1] + 1].ITEM = "Busy"
                        if unplaced_ship.CELL[1]-1 > -1:
                            data.enemy_map[unplaced_ship.CELL[0] - value_edit][unplaced_ship.CELL[1] - 1].ITEM = "Busy"
                        data.enemy_map[unplaced_ship.CELL[0] - value_edit][unplaced_ship.CELL[1]].ITEM = "Busy"
                elif unplaced_ship.ANGLE == 0:
                    if unplaced_ship.CELL[1] + value_edit > -1 and unplaced_ship.CELL[1] + value_edit < 10 and unplaced_ship.CELL[1] - value_edit < 10 and unplaced_ship.CELL[1] - value_edit > -1:
                        if unplaced_ship.CELL[0]+1 < 10:
                            data.enemy_map[unplaced_ship.CELL[0] + 1][unplaced_ship.CELL[1] + value_edit].ITEM = "Busy"
                        if unplaced_ship.CELL[0]-1 > -1:
                            data.enemy_map[unplaced_ship.CELL[0] - 1][unplaced_ship.CELL[1] + value_edit].ITEM = "Busy"
                        data.enemy_map[unplaced_ship.CELL[0]][unplaced_ship.CELL[1] + value_edit].ITEM = "Busy"
        if unplaced_ship.TYPE == "Mini":
            place_busy_cells_plus(1,ship)
        if unplaced_ship.TYPE == "Normal":
            place_busy_cells_plus(2,ship)
        if unplaced_ship.TYPE == "Big":
            place_busy_cells_plus(3,ship)
        if unplaced_ship.TYPE == "Huge":
            place_busy_cells_plus(4,ship)
    def ship_placement_done(unplaced_ship):
        global ships
        # print(f"Type: {data.unplaced_ship.TYPE} \nAngle: {data.unplaced_ship.ANGLE}")
        data.ships.append(unplaced_ship)
        data.ships[-1].cell_ship()
        return sh.Ship(cell = [0,0,0], type = ship, side = "Enemy", angle = 0)
        
    
        
    for ship in ships:
    #     if   unplaced_ship.TYPE == "Mini":       lenght = 1
    #     elif unplaced_ship.TYPE == "Normal":     lenght = 2
    #     elif unplaced_ship.TYPE == "Big":        lenght = 3
    #     elif unplaced_ship.TYPE == "Huge":       lenght = 4
        place_end = True
        
        while place_end:
            unplaced_ship.ANGLE = random.randint(0, 3) * 90
            unplaced_ship.CELL = [random.randint(0, 9), random.randint(0, 9)]
            if unplaced_ship.TYPE   == "Mini":      lenght = 0
            elif unplaced_ship.TYPE == "Normal":    lenght = 1
            elif unplaced_ship.TYPE == "Big":       lenght = 2
            elif unplaced_ship.TYPE == "Huge":      lenght = 3
            # if unplaced_ship.ANGLE == 90:           unplaced_ship.CELL[0] -= lenght
            if unplaced_ship.ANGLE == 180:          unplaced_ship.CELL[1] -= lenght 
            if unplaced_ship.ANGLE == 270:          unplaced_ship.CELL[0] += lenght 
            approval = check_cells(unplaced_ship)
            if approval:
                place_busy_cells(unplaced_ship)
                unplaced_ship = ship_placement_done(unplaced_ship)
                place_end = False 
def enemy_shoot(frame):
    global shoot
    global target
    global sides
    global line
    global line_lenght 
    global end_of_line
    global side
    global repeat
    global line_ready
    shoot_place = True
    busy=0
    # print(shoot, target, len(sides), repeat)
    if frame % 30 == 0:
        if target == "Ship":
            print(line)
            if line == 0:
                print(f"passed line check, {repeat}")
                if len(sides)== 0:
                    print("sides: 0")
                    sides = "Вот этому" ; sides = [[-1, 0],[0, -1],  [0, 1], [1, 0]]
                if repeat == 0:
                    print("repeat: 0")
                    repeat = len(sides)
                for r in range(repeat):
                    print(f"Side repeater activated: {side}")
                    repeat -= 1
                    print(3 - abs(len(sides)-3), len(sides))
                    side = sides[random.randint(0, 3 - abs(len(sides)-4))]
                    sides.remove(side)
                    if shoot_place:
                        print("shoot_place check passed")
                        if 0 <= shoot[0] + side[0] <= 9 and 0 <= shoot[1] + side[1] <= 9:
                            print("border check passed")
                            if data.player_map[shoot[0] + side[0]][shoot[1] + side[1]].EFFECT == 0:
                                if data.player_map[shoot[0] + side[0]][shoot[1] + side[1]].ITEM == "Busy" or data.player_map[shoot[0] + side[0]][shoot[1] + side[1]].ITEM == 0:
                                    data.player_map[shoot[0] + side[0]][shoot[1] + side[1]].EFFECT = "cross"
                                    print("miss")
                                    shoot_place = False
                                    repeat = len(sides)
                                    return True
                                elif data.player_map[shoot[0] + side[0]][shoot[1] + side[1]].ITEM == "Ship":
                                    data.player_map[shoot[0] + side[0]][shoot[1] + side[1]].EFFECT = "explosion"
                                    print(f"Boom, line info: {line_ready, line}")
                                    print(f"Side: {side}")
                                    shoot = [shoot[0] + side[0],shoot[1] + side[1]]
                                    shoot = [shoot[0] + side[0],shoot[1] + side[1]]
                                    sides = [[-1, 0],[0, -1],  [0, 1], [1, 0]]
                                    if line_ready == True:
                                        line = side
                                        print("Targeted ship hunting done. Line started.")
                                    line_lenght = 3
                                    repeat = len(sides)
                                    return False
                                else: print(data.player_map[shoot[0] + side[0]][shoot[1] + side[1]].ITEM)
                            else:
                                busy += 1     
                        else: print("busy_plus"); busy += 1
                if busy == 4:
                    repeat = 4
                    print("all busy")
                    target = 0
                    shoot = [0, 0]
                    line_ready = 0
                    shoot_place = False
            else: 
                print("Line_attack")
                if -1 < shoot[0] < 10 and -1 < shoot[1] < 10:
                    print("Line attack in the borders")
                    if data.player_map[shoot[0]][shoot[1]].EFFECT == 0:
                        print("Line attack: passed effect check")
                        if end_of_line==0:
                            if data.player_map[shoot[0]][shoot[1]].ITEM == 0 or data.player_map[shoot[0]][shoot[1]].ITEM == "Busy":                   
                                prev_shoot = shoot
                                if   side == [1, 0]:    shoot = [shoot[0]-line_lenght, shoot[1]];   end_of_line=2
                                elif side == [-1, 0]:   shoot = [shoot[0]+line_lenght, shoot[1]];   end_of_line=2
                                elif side == [0, 1]:    shoot = [shoot[0], shoot[1]-line_lenght];   end_of_line=2
                                elif side == [0, -1]:   shoot = [shoot[0] ,shoot[1]+line_lenght];   end_of_line=2
                                shoot_place = True
                                data.player_map[prev_shoot[0]][prev_shoot[1]].EFFECT = "cross"
                                return True
                        if end_of_line == 1:
                            if  data.player_map[shoot[0]][shoot[1]].ITEM == 0 or  data.player_map[shoot[0]][shoot[1]].ITEM == "Busy":
                                print(f"More info: \n   Side: {side} \n   Item on current cell: {data.player_map[shoot[0]][shoot[1]].ITEM} \n   Coordinates: ({shoot})")
                                data.player_map[shoot[0]][shoot[1]].EFFECT = "cross"
                                target = 0
                                side = 0
                                end_of_line = 0
                                shoot = 0
                                line_ready = 0
                                end_of_line = 0
                                shoot_place = 1
                                line = 0
                                return True
                        if data.player_map[shoot[0]][shoot[1]].ITEM == "Ship" and end_of_line==1:
                            shoot_place = 1
                            data.player_map[shoot[0]][shoot[1]].EFFECT = "explosion"
                            shoot = [shoot[0] - side[0],shoot[1] - side[1]]
                            return False
                        elif data.player_map[shoot[0]][shoot[1]].ITEM == "Ship" and end_of_line==0:
                            shoot_place = 1
                            data.player_map[shoot[0]][shoot[1]].EFFECT = "explosion"
                            shoot = [shoot[0] + side[0],shoot[1] + side[1]]
                            line_lenght += 1
                            return False
                        elif data.player_map[shoot[0]][shoot[1]].ITEM == "Ship" and end_of_line==2:
                            print("end happen. explosion")
                            shoot_place = 1
                            data.player_map[shoot[0]][shoot[1]].EFFECT = "explosion"
                            shoot = [shoot[0] - side[0],shoot[1] - side[1]]
                            end_of_line = 1
                            return False 
                        elif end_of_line == 2:
                            if data.player_map[shoot[0]][shoot[1]].ITEM == 0 or data.player_map[shoot[0]][shoot[1]].ITEM == "Busy" and end_of_line == 2:
                                print("Okay, line end")
                                data.player_map[shoot[0]][shoot[1]].EFFECT = "cross"
                                target = 0
                                side = 0
                                line = 0
                                line_ready = 0
                                end_of_line = 0
                                shoot = 0
                                end_of_line = 0
                                shoot_place = 0
                                return True
                        else:
                            print(f"Not passed effect - check. \nMore info: \n   Side - {side} \n   Effect at this cell: {data.player_map[shoot[0]][shoot[1]].EFFECT} \n   Coordinates: ({shoot}) \n   Line lenght: {line_lenght} \n   End of line: {end_of_line}")
                    else:
                        print(f"Not passed effect - check. \nMore info: \n   Side - {side} \n   Effect at this cell: {data.player_map[shoot[0]][shoot[1]].EFFECT} \n   Coordinates: ({shoot}) \n   Line lenght: {line_lenght}")
                        if end_of_line == 0:
                            print("The line isn`t end")
                            print(side, f"({shoot[0]}, {shoot[1]})")
                            prev_shoot = shoot
                            if   side == [1, 0]:    shoot = [shoot[0]-line_lenght,shoot[1]];   end_of_line=2
                            elif side == [-1, 0]:   shoot = [shoot[0]+line_lenght,shoot[1]];   end_of_line=2
                            elif side == [0, 1]:    shoot = [shoot[0],shoot[1]-line_lenght];   end_of_line=2
                            elif side == [0, -1]:   shoot = [shoot[0],shoot[1]+line_lenght];   end_of_line=2
                            if data.player_map[prev_shoot[0]][prev_shoot[1]].EFFECT == 0:
                                data.player_map[prev_shoot[0]][prev_shoot[1]].EFFECT = "cross"
                                print("cross vizualized")
                                return True
                            else:
                                print(f"Cross vizualization fail.   Info about fail: \n   Effect: {data.player_map[prev_shoot[0]][prev_shoot[1]].EFFECT} \n   Coordinates: ({prev_shoot})")
                                return False
                        else:
                            print("Okay, line end")
                            prev_shoot = shoot
                            target = 0
                            side = 0
                            line = 0
                            line_ready = 0
                            end_of_line = 0
                            shoot = 0
                            end_of_line = 0
                            shoot_place = 0
                            if data.player_map[prev_shoot[0]][prev_shoot[1]].EFFECT == 0:
                                data.player_map[prev_shoot[0]][prev_shoot[1]].EFFECT = "cross"
                                return True
                            else: 
                                print(f"Cross vizualization fail.   Info about fail: \n   Effect: {data.player_map[prev_shoot[0]][prev_shoot[1]].EFFECT} \n   Coordinates: ({prev_shoot})")
                                return False
                else:
                    print("Out of borders")
                    if end_of_line == 0:
                        print("No end")
                        prev_shoot = shoot
                        if   side == [1, 0]:    shoot = [shoot[0]-line_lenght,shoot[1]];   end_of_line=2
                        elif side == [-1, 0]:   shoot = [shoot[0]+line_lenght,shoot[1]];   end_of_line=2
                        elif side == [0, 1]:    shoot = [shoot[0],shoot[1]-line_lenght];   end_of_line=2
                        elif side == [0, -1]:   shoot = [shoot[0],shoot[1]+line_lenght];   end_of_line=2
                        if -1 < prev_shoot[0] < 10 and -1 < prev_shoot[1] < 10:
                            if data.player_map[prev_shoot[0]][prev_shoot[1]].EFFECT == 0:
                                print("Cross vizualization succeful!")
                                data.player_map[prev_shoot[0]][prev_shoot[1]].EFFECT = "cross"
                                return True
                            else:
                                print(f"Cross vizualization fail.   Info about fail: \n   Coordinates: ({prev_shoot})")
                                return False
                        else:
                            print(f"Cross vizualization fail.   Info about fail: \n   Coordinates: ({prev_shoot})")
                            return False
                    elif end_of_line == 1 or end_of_line == 2:
                        print("End of line")
                        prev_shoot = shoot
                        target = 0
                        side = 0
                        line = 0
                        end_of_line = 0
                        shoot = 0
                        line_ready = 0
                        end_of_line = 0
                        shoot_place = 0
                        if -1 < prev_shoot[0] < 10 and -1 < prev_shoot[1] < 10:
                            if data.player_map[prev_shoot[0]][prev_shoot[1]].EFFECT == 0:
                                data.player_map[prev_shoot[0]][prev_shoot[1]].EFFECT = "cross"
                                return True
                            else:
                                print(f"Cross vizualization fail.   Info about fail: \n   Coordinates: ({prev_shoot})")
                                return False
                        else:
                            print(f"Cross vizualization fail.   Info about fail: \n   Coordinates: ({prev_shoot})")
                            return False
    elif target == 0: 
        cell = [random.randint(0, 9), random.randint(0, 9)]
        if data.player_map[cell[0]][cell[1]].EFFECT == 0:
            if data.player_map[cell[0]][cell[1]].ITEM == 0:
                data.player_map[cell[0]][cell[1]].EFFECT = "cross"
                print("miss")
                return True
            elif data.player_map[cell[0]][cell[1]].ITEM == "Ship": 
                data.player_map[cell[0]][cell[1]].EFFECT = "explosion"
                target = "Ship"
                print("Boom")
                shoot = [cell[0],cell[1]]
                line_ready = True
                return False