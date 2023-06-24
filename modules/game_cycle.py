import pygame, os
import modules.data_base as data
import modules.ship as ship
import modules.click_and_hover_detection as click
import modules.place_player_ships as pps
import modules.enemy as enemy
import modules.button as button
import modules.win as win
step = "Player"
res_button = button.Button(400,10,200,100)
# Створюємо об'єкт з фпс 
FPS = pygame.time.Clock()
# Змінна циклу
game_cycle = 1
enemy.place_enemy_ships()
# Задаємо розміри екрану
screen = pygame.display.set_mode((1000,700))
repeat = 0
# Цикл з умовою котрий працює поки game_cycle == 1
while game_cycle:
    # Який буде фпс
    FPS.tick(60)
    # Заповнення екрану
    if repeat % 5 == 0:
        screen.fill((255,255,255))
        screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(os.path.abspath("images\\background.jpg"))), (1000,700)), (0,0))
        win.win_counter.win_blit(screen)
        
    if repeat % 5 == 0:
        
        if win.win_check() != None:
            data.win = 0
        win.blit_win(screen)
        
    # цикл для каждого события 
    
    for event in pygame.event.get():
        # условие с проверкой открыта ли игра
        if event.type == pygame.QUIT:
            # переменная с цикла 
            game_cycle = 0
        # проверка нажата ли кнопка
        if pps.current_ship > 10:
            if step == "Player" and data.win:
                if click.click_hover_detection(event):
                    step = "Enemy"
            
        
        if pps.current_ship <= 10:
            pps.controls()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print("меня хотят перетянуть")
                if data.unplaced_ship.TYPE != "Hover":
                    pps.choose_ship()
                
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                pps.placement_finish()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Нажали: {pygame.mouse.get_pos()}\nА можно только в: \n   X: {res_button.X}---{res_button.X+res_button.WIDTH}\n   Y: {res_button.Y}---{res_button.Y+res_button.HEIGHT}")
            if res_button.X < pygame.mouse.get_pos()[0] < res_button.X + res_button.WIDTH and res_button.Y < pygame.mouse.get_pos()[1] < res_button.Y + res_button.HEIGHT:
                res_button.click_button("Click")
        elif event.type == pygame.MOUSEBUTTONUP:
            if res_button.X < pygame.mouse.get_pos()[0] < res_button.X + res_button.WIDTH and res_button.Y < pygame.mouse.get_pos()[1] < res_button.Y + res_button.HEIGHT:
                step = "Player"
                res_button.click_button("Up")
                data.win = 1
            else: res_button.STATE = "unpressed"
    # фон для игры 
    if data.unplaced_ship.STATE == "Hover": pps.replace_ship(); pps.controls()
    
    # цикл для риссование клеточек
    for count in range(10):
        # цикл для отрисовывание клеток игрока 
        if repeat % 5 == 0:
            for cell in data.player_map[count]:
                # отрисовывание клетки
                cell.blit_cell(screen)
        # цикл для  отрисовывание клеток противника
        for cell in data.enemy_map[count]:
            # отрисовывание клетки 
            cell.blit_cell(screen)
        

    # отображение кораблей
    if repeat % 5==0:
        for ship1 in data.ships:
            if ship1.SIDE == "Player": ship1.blit_ship(screen=screen) 
            # print(ship1.TYPE)
    if repeat % 5 == 0:
        for row in data.player_map:
            for cell in row:
                cell.effect_blit(screen)
    for row in data.enemy_map:
        for cell in row:
            cell.effect_blit(screen)
    if repeat % 5 == 0 and pps.current_ship < 11:
        data.unplaced_ship.blit_ship(screen=screen)
    res_button.blit_button(screen)
    destroy_count = 0
    # click.click_hover_detection()
    # обновление
    # print(f"unplaced: {data.unplaced_ship}; placed: {data.ships}")
    if step == "Enemy" and data.win:
        if enemy.enemy_shoot(repeat):
            step = "Player"
    pygame.display.flip()
    repeat += 1
        