import pygame
import sys
import math
import time
import threading
import random
def player_event(player_image,player_rect,player_speed):
    # 取得鼠標位置
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # 更新玩家位置
    player_rect.centerx = mouse_x
    player_rect.centery = mouse_y
    
    
    screen.blit(player_image, player_rect)
    

def bullet_event(bullets,bullet_speed,bullet_image):
     # 更新彈幕位置
    for bullet in bullets:
        bullet.centery -= bullet_speed
        if bullet.centery <= 0:
            bullets.remove(bullet)
    for bullet in bullets:
        screen.blit(bullet_image, bullet)


def ui_event(width,height,bullets):

    # 創建文本
    font = pygame.font.Font(None, 36)  #字體與大小(None 默認字體)

    # 創建對象
    text = font.render(f"Score: {score}", True, white)

    # 獲取文本對象
    text_rect = text.get_rect()

    # 設置文本位置
    text_rect.centerx = 100
    text_rect.centery = 20
    screen.blit(text, text_rect)

def game_system(monsters,battle_status):
    if battle_status==0:
        battle_status +=1
    

    return battle_status



def monster_battle_type_one(monsters,monster_image,radius,monster_speed,angle):
    for i in range(len(monsters)):
        if i  == 0:
            # 計算monster在弧線上的位置
            monsters[i].centerx  += int(radius * math.cos(math.radians(angle)))*monster_speed
            monsters[i].centery  +=  int(radius * math.sin(math.radians(angle)))*monster_speed
            # 增加角度，使monster在弧線上移動
            screen.blit(monster_image,monsters[i])
        if i  == 1:
            # 計算monster在弧線上的位置
            monsters[i].centerx  -= int(radius * math.cos(math.radians(-angle)))*monster_speed
            monsters[i].centery  -=  int(radius * math.sin(math.radians(-angle)))*monster_speed
            # 增加角度，使monster在弧線上移動
            screen.blit(monster_image,monsters[i])
        if i == 2:
            # 計算monster在弧線上的位置
            monsters[i].centery  += monster_speed
        
            # 增加角度，使monster在弧線上移動
            screen.blit(monster_image,monsters[i])

   




def monster_event(monster_image,radius,angle,monsters,monster_speed,battle_status):
    #monster position
    match battle_status:
        case 1:
            if angle >=90:
                monster_speed = 0
            monster_battle_type_one(monsters,monster_image,radius,monster_speed,angle)
            
def creat_monster(monster_rect,monsters):
    for i in range(3):
        monster_rect.centerx = width // 2
        monster_rect.centery = 50
        monster = monster_rect.copy()
        monsters.append(monster)


def object_collider(game_object, other_object, player_object, monster_bullet_object,monster_bullet_object_map):
    # 碰撞检测
    global score
    for monster in game_object:
        for bullet in other_object: #bullet and monster
            try:
                if monster.colliderect(bullet):
                    score +=10
                    other_object.remove(bullet)
            except:
                pass
        if player_object.colliderect(monster): #player and monster
            # print("Player has been hurt")
            pass
    
    for monster_bullet_rect in monster_bullet_object:
        
        try:
            if player_object.colliderect(monster_bullet_rect) and object_can_destroy == True:
                monster_bullet_object.remove(monster_bullet_rect)
        except:
            pass
        if player_object.colliderect(monster_bullet_rect): #player and monster_bullet
            print("Player has been hurt by monster_bullet")
    for monster_bullet_map_rect in monster_bullet_object_map:
        try:
            if player_object.colliderect(monster_bullet_map_rect):
                print("Player has been hurt by monster_bullet_map")
        except:
            pass
            
        
def monster_attack_type_one(y_pos):
    global last_bullet_time
    global monster_bullet_image
    global monster_bullet
    global monster_bullet_rect
    global monster_bullet_speed
    global object_can_destroy
    object_can_destroy = True
    
    # 当前时间
    current_time = time.time()

    if current_time - last_bullet_time >= 1:
        monster_bullet_rect.centery = y_pos
        monster_bullet_rect.centerx = 0
        bullet = monster_bullet_rect.copy()
        monster_bullet.append(bullet)
        monster_bullet_rect.centery = y_pos+100
        monster_bullet_rect.centerx = 0
        bullet = monster_bullet_rect.copy()
        monster_bullet.append(bullet)
        last_bullet_time = current_time
    try:

        for bullet in monster_bullet:
            if bullet.centerx <=width:
                bullet.centerx +=6
                screen.blit(monster_bullet_image,bullet)
            else:
                monster_bullet.remove(bullet)

       
    except:
        pass


def monster_attack_type_two(y_pos):
    global last_bullet_time
    global monster_bullet_image
    global monster_bullet
    global monster_bullet_rect
    global player_rect
    global monster_bullet_speed
    global object_can_destroy
    object_can_destroy = True
    # 当前时间
    current_time = time.time()
    if current_time - last_bullet_time >= 1:
        monster_bullet_rect.centery = y_pos
        monster_bullet_rect.centerx = 0
        bullet = monster_bullet_rect.copy()
        monster_bullet.append(bullet)
        last_bullet_time = current_time
    try:
        for bullet in monster_bullet:
            if bullet.centerx <=width:
                if  bullet.centerx <player_rect.centerx and bullet.centery == y_pos:
                    bullet.centerx +=6
                    screen.blit(monster_bullet_image,bullet)
                else:
                    bullet.centery +=10
                    screen.blit(monster_bullet_image,bullet)
            else:
                monster_bullet.remove(bullet)
    except:
        pass

def monster_attack_type_nine(y_pos):
    global last_bullet_time
    global monster_bullet_image
    global monster_bullet
    global monster_bullet_rect
    global player_rect
    global monster_bullet_speed
    global object_can_destroy
    object_can_destroy = True
    # 当前时间
    current_time = time.time()
    if current_time - last_bullet_time >= 1:
        monster_bullet_rect.centery = y_pos
        monster_bullet_rect.centerx = 0
        bullet = monster_bullet_rect.copy()
        monster_bullet.append(bullet)
        last_bullet_time = current_time
    try:
        for bullet in monster_bullet:
            if bullet.centerx <=width:
                if  bullet.centerx <player_rect.centerx and bullet.centery == y_pos:
                    bullet.centerx +=6
                    screen.blit(monster_bullet_image,bullet)
                else:
                    bullet.centery -=10
                    screen.blit(monster_bullet_image,bullet)
            else:
                monster_bullet.remove(bullet)
    except:
        pass




def monster_attack_type_seven(x_pos):
    global last_bullet_time
    global monster_bullet_image
    global monster_bullet
    global monster_bullet_rect
    global player_rect
    global monster_bullet_speed
    global object_can_destroy
    object_can_destroy = True
    # 当前时间
    current_time = time.time()
    if current_time - last_bullet_time >= 1:
        monster_bullet_rect.centery = 0
        monster_bullet_rect.centerx = x_pos
        bullet = monster_bullet_rect.copy()
        monster_bullet.append(bullet)
        last_bullet_time = current_time
    try:
        for bullet in monster_bullet:
            if bullet.centery <=height:
                if bullet.centery < player_rect.centery and bullet.centerx == x_pos:
                    bullet.centery +=6
                    screen.blit(monster_bullet_image,bullet)
                else:
                    bullet.centerx +=10
                    screen.blit(monster_bullet_image,bullet)
            else:
                monster_bullet.remove(bullet)
    except:
        pass
def monster_attack_type_eight(x_pos):
    global last_bullet_time
    global monster_bullet_image
    global monster_bullet
    global monster_bullet_rect
    global player_rect
    global monster_bullet_speed
    global object_can_destroy
    object_can_destroy = True
    # 当前时间
    current_time = time.time()
    if current_time - last_bullet_time >= 1:
        monster_bullet_rect.centery = 0
        monster_bullet_rect.centerx = x_pos
        bullet = monster_bullet_rect.copy()
        monster_bullet.append(bullet)
        last_bullet_time = current_time
    try:
        for bullet in monster_bullet:
            if bullet.centery <=height:
                if bullet.centery < player_rect.centery and bullet.centerx == x_pos:
                    bullet.centery +=6
                    screen.blit(monster_bullet_image,bullet)
                else:
                    bullet.centerx -=10
                    screen.blit(monster_bullet_image,bullet)
            else:
                monster_bullet.remove(bullet)
    except:
        pass

#待修
def monster_attack_type_three(y_pos, x_pos):
    global last_bullet_time
    global monster_bullt_scale_factor
    global monster_bullet_image
    global monster_bullet
    global monster_bullet_rect
    global monster_bullet_speed
    global width
    global height
    global direction_x 
    global direction_y 
    global object_can_destroy
    object_can_destroy = True

    # 当前时间
    current_time = time.time()

    if current_time - last_bullet_time >= 1 and len(monster_bullet) < 1 :
        new_bullet_rect = monster_bullet_rect.copy()
        new_bullet_rect.centerx = 0
        new_bullet_rect.centery = 0
        monster_bullet.append(new_bullet_rect)
        scaled_image = pygame.transform.scale(monster_bullet_image, (
                    int(monster_bullet_image.get_width() * 0),
                    int(monster_bullet_image.get_height() * 0)))
        screen.blit(scaled_image, monster_bullet[0])
        last_bullet_time = current_time
    try:
        for i in range(len(monster_bullet)):
            max_scale = 8
            if monster_bullt_scale_factor <=max_scale:
                monster_bullt_scale_factor +=0.1
              
                scaled_image = pygame.transform.scale(monster_bullet_image, (
                    int(monster_bullet_image.get_width() * monster_bullt_scale_factor),
                    int(monster_bullet_image.get_height() * monster_bullt_scale_factor)))
                
                rect = scaled_image.get_rect()
                rect.width = scaled_image.get_width() *0.8
                rect.height = scaled_image.get_height() *0.8
                rect.centerx = width /2
                rect.centery = height /2
                monster_bullet[0] = rect
       

                screen.blit(scaled_image, monster_bullet[0])
                
            else:
                monster_bullt_scale_factor = 0.1
                monster_bullet.remove(monster_bullet[0])
                pass
                
    except:
        pass
def monster_attack_type_fore(y_pos, x_pos):
    global object_can_destroy
    global last_bullet_time
    global monster_bullt_scale_factor
    global monster_bullet_image
    global monster_bullet
    global monster_bullet_rect
    global monster_bullet_speed
    global width
    global height
    global direction_x 
    global direction_y 
    object_can_destroy = True
    # 当前时间
    current_time = time.time()

    if current_time - last_bullet_time >= 1 and len(monster_bullet) < 1 :
        new_bullet_rect = monster_bullet_rect.copy()
        new_bullet_rect.centerx = 0
        new_bullet_rect.centery = 0
        monster_bullet.append(new_bullet_rect)
        scaled_image = pygame.transform.scale(monster_bullet_image, (
                    int(monster_bullet_image.get_width() * 0),
                    int(monster_bullet_image.get_height() * 0)))
        screen.blit(scaled_image, monster_bullet[0])
        last_bullet_time = current_time
    try:
        for i in range(len(monster_bullet)):
            max_scale = 6
            if monster_bullt_scale_factor <=max_scale:
                monster_bullt_scale_factor +=0.1
              
                scaled_image = pygame.transform.scale(monster_bullet_image, (
                    int(monster_bullet_image.get_width() * monster_bullt_scale_factor),
                    int(monster_bullet_image.get_height() * monster_bullt_scale_factor)))
                
                rect = scaled_image.get_rect()
                rect.width = scaled_image.get_width() *0.8
                rect.height = scaled_image.get_height() *0.8
                rect.centerx = width /2
                rect.centery = height /2 +40
                monster_bullet[0] = rect
                if rect.centerx-x_pos >0:
                    direction_x = -1
                else :
                    direction_x = 1
                if rect.centery-y_pos >0:
                    direction_y = -1
                else :
                    direction_y = 1

                screen.blit(scaled_image, monster_bullet[0])
            elif monster_bullt_scale_factor >max_scale and monster_bullt_scale_factor <=max_scale +1  and monster_bullet[0].centerx !=0 and monster_bullet[0].centery !=0:
                scaled_image = pygame.transform.scale(monster_bullet_image, (
                    int(monster_bullet_image.get_width() * max_scale),
                    int(monster_bullet_image.get_height() * max_scale)))
                monster_bullt_scale_factor +=0.01
                if  abs(monster_bullet[0].centerx - x_pos)>10 and monster_bullet[0].centerx - x_pos !=0:
                    
                    monster_bullet[0].centerx +=direction_x*monster_bullet_speed
                if  abs(monster_bullet[0].centery - y_pos)>10  and monster_bullet[0].centery - y_pos !=0:
                    
                    monster_bullet[0].centery +=direction_y*monster_bullet_speed
                
                screen.blit(scaled_image, monster_bullet[0])
            else:
                monster_bullt_scale_factor = 0.1
                monster_bullet.remove(monster_bullet[0])
    except:
        pass
def monster_attack_type_five():
    global object_can_destroy
    global last_bullet_time
    global side_width
    global side_length
    global monster_bullet_angle
    global monster_bullet
    global monster_speed
    global monster_bullet_map
    global player_rect
    object_can_destroy = False
    side_length = 20
    max_width = width


    try:
        white = (255, 255, 255)
        rect = pygame.Rect((width // 2 , 0 - 50, 20, 20))  # 正方形的位置和大小
        
        
        
        if len(monster_bullet_map) <3:
           
            monster_bullet_map.append(rect)
            
       

        monster_bullet_map[1].centerx = monster_bullet_map[0].centerx + 250
        monster_bullet_map[2].centerx = monster_bullet_map[0].centerx - 250


        for i in range(len(monster_bullet_map)):
            if side_width <= max_width:
                side_width +=1
            monster_bullet_map[i].height = side_width
            pygame.draw.rect(screen, white, monster_bullet_map[i])
        if monster_bullet_map[0].height >= max_width:
            monster_attack_type_two(10)
       
    except:
        pass

def monster_attack_type_six():
    global object_can_destroy
    global last_bullet_time
    global side_width
    global side_length
    global monster_bullet_angle
    global monster_bullet
    global monster_speed
    global monster_bullet_map
    global player_rect
    object_can_destroy = False
 
    max_width = width
    max_length = height+300



    try:
        white = (255, 255, 255)
        rect = pygame.Rect((0 , 0 , 20, 20))  # 正方形的位置和大小
        rect_2 = pygame.Rect((0 , 0 , 20, 20)) 
       
        
        if len(monster_bullet_map) <2:
            
            monster_bullet_map.append(rect)
        if  len(monster_bullet_map) >=2 and len(monster_bullet_map) <4:
            monster_bullet_map.append(rect_2)

        monster_bullet_map[0].centerx =width-250
        monster_bullet_map[1].centerx = 250


        monster_bullet_map[2].centery = height-250
        monster_bullet_map[3].centery = 250



        if side_length <= max_length:
            side_length +=2

        if side_width <= max_width:
            side_width +=2

        for i in range(2):
            
           
            monster_bullet_map[i].height = side_width
            pygame.draw.rect(screen, white, monster_bullet_map[i])


        for i in range(2):
            
            monster_bullet_map[i+2].width = side_length
            pygame.draw.rect(screen, white, monster_bullet_map[i+2])

        print(max_length)

        if side_width >= max_width :
            monster_attack_type_two(10)
          
    except:
        pass
def monster_attacK_type_ten(y_pos):
    global last_bullet_time
    global monster_bullet_image
    global monster_bullet
    global monster_bullet_rect
    global monster_bullet_speed
    global object_can_destroy
    object_can_destroy = True
    
    # 当前时间
    current_time = time.time()

    if current_time - last_bullet_time >= 1:
        monster_bullet_rect.centery = y_pos
        monster_bullet_rect.centerx = 0
        bullet = monster_bullet_rect.copy()
        monster_bullet.append(bullet)
        monster_bullet_rect.centery = y_pos+100
        monster_bullet_rect.centerx = 0
        bullet = monster_bullet_rect.copy()
        monster_bullet.append(bullet)
        monster_bullet_rect.centery = y_pos+200
        monster_bullet_rect.centerx = 0
        bullet = monster_bullet_rect.copy()
        monster_bullet.append(bullet)
        monster_bullet_rect.centery = y_pos+300
        monster_bullet_rect.centerx = 0
        bullet = monster_bullet_rect.copy()
        monster_bullet.append(bullet)
        last_bullet_time = current_time
    try:

        for bullet in monster_bullet:
            if bullet.centerx <=width :
                bullet.centerx +=6
                screen.blit(monster_bullet_image,bullet)
            else:
                monster_bullet.remove(bullet)

       
    except:
        pass
    
    



def monster_attack():
    global current_attack_mode, last_attack_change_time,monster_bullet,monster_bullet_map,side_width,side_length,monster_bullt_scale_factor,score
    


    

    
    if current_attack_mode == 0:
            current_attack_mode= random.randint(1, 10)


    current_time = pygame.time.get_ticks()
    if current_time - last_attack_change_time >= 30000:  # 30秒切换一次
        score +=100
        current_attack_mode = (current_attack_mode + 1) % 10
        last_attack_change_time = current_time
        last_attack_mode = random.randint(1, 10)
        if last_attack_mode !=current_attack_mode:
            monster_bullet = []
            monster_bullet_map = []
            side_width = 0
            side_length = 0
            monster_bullt_scale_factor = 0
            current_attack_mode=last_attack_mode
        print(last_attack_mode)
    
    match current_attack_mode:
        case 1:
            monster_attack_type_one(300)
        case 2:
            monster_attack_type_two(10)
        case 3:
            # monster_attack_type_three(player_rect.centery,player_rect.centerx)
            monster_attack_type_fore(player_rect.centery,player_rect.centerx)
        case 4:
            monster_attack_type_fore(player_rect.centery,player_rect.centerx)
        case 5:     
            monster_attack_type_five()
        case 6:
            monster_attack_type_six()
        case 7:
            monster_attack_type_seven(10)
        case 8:
            monster_attack_type_eight(width-10)
        case 9:
            monster_attack_type_nine(height-10)
        case 10:
            monster_attacK_type_ten(200)
  
    pass
    
if  __name__ == '__main__':  
    # 初始化Pygame
    pygame.init()
    # 設置畫面
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))

    #設置畫面標題
    pygame.display.set_caption("Danmaku Game")

    #顏色
    white = (255, 255, 255)
    black = (0, 0, 0)


    # 遊戲LOOP
    clock = pygame.time.Clock()
    # 在遊戲LOOP前添加

    # player
    player_image = pygame.image.load("img\player.png")
    player_scale_factor = 0.1
    player_image = pygame.transform.scale(player_image, (int(player_image.get_width() * player_scale_factor), int(player_image.get_height() * player_scale_factor)))
    player_rect = player_image.get_rect()
    player_rect.width = player_image.get_width()*0.8
    player_speed = 5

    #player_bullet
    bullet_image = pygame.image.load("img\player_bullet.png")
    bullet_scale_factor =0.1
    bullet_image = pygame.transform.scale(bullet_image,(int(bullet_image.get_width()*bullet_scale_factor),int(bullet_image.get_height()*bullet_scale_factor)))
    bullet_rect = bullet_image.get_rect()
    bullet_speed = 8
    bullets = []    

    # monster
    monster_image = pygame.image.load("img\monster_1.png")
    monster_scale_factor = 0.1
    monster_image = pygame.transform.scale(monster_image,(int(monster_image.get_width()*monster_scale_factor),int(monster_image.get_height()*monster_scale_factor)))
    monster_rect = monster_image.get_rect()
    monster_speed = 1
    monsters =[]
    angle = 0  # 初始角度
    radius = 3  # 弧線半徑
  
    #monster bullet
    monster_bullet_image = pygame.image.load("img/bullet_1.png")
    monster_bullt_scale_factor = 0.1
    monster_bullet_image = pygame.transform.scale(monster_bullet_image,(int(monster_bullet_image.get_width()*monster_bullt_scale_factor),int(monster_bullet_image.get_height()*monster_bullt_scale_factor)))
    monster_bullet_rect = monster_bullet_image.get_rect()
    monster_bullet_speed = 1
    
    last_bullet_time = time.time()
    monster_bullet = []
    monster_bullet_map = []
    side_width = 0
    side_length = 0

     

    #game_system
    battle_status = 0
    full_monster = None
    can_creat = True
    object_can_destroy = False
    score = 0
    current_attack_mode = 0
    last_attack_change_time = pygame.time.get_ticks()


    creat_monster(monster_rect,monsters)
    



    while True:
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 發射彈幕
                bullet = bullet_rect.copy()
                bullet.centerx = player_rect.centerx
                bullet.centery = player_rect.centery
                bullets.append(bullet)
            
            
       
       
        #清空畫面
        screen.fill(black)
        #更新player位置
        player_event(player_image,player_rect,player_speed)
        #更新彈幕位置
        bullet_event(bullets,bullet_speed,bullet_image)
        
        battle_status = game_system(monsters,battle_status)
        # battle_status = 1
       # 在游戏循环中调用
        object_collider(monsters, bullets, player_rect,monster_bullet,monster_bullet_map)
        
        # 当怪物列表为空时增加 battle_status
        if len(monsters) == 0:
            creat_monster(monster_rect,monsters)
            battle_status+=1
        if battle_status == 1:
           monster_attack()

        # monster_attack()
    





        if battle_status == 1 and angle <180:
            angle += 1
      
        monster_event(monster_image,radius,angle,monsters,monster_speed,battle_status)
        
       


        # 更新UI
        ui_event(width,height,bullets)
       

        # 畫面UPDATE
        pygame.display.update()
        clock.tick(60)

