import os
import pygame
############################################################
# 기본 초기화 (반드시 해야 하는 것)
pygame.init() # 초기화 (반드시 필요)

# Window Size
screen_width = 640 
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

#Title setting
pygame.display.set_caption("Bubble Gun") #Name of game

#FPS
clock = pygame.time.Clock()
#############################################################

#1. 사용자 게임 초기화 (배경, 게임이미지, 좌표, 폰트 설정, 이동속도)
current_path = os.path.dirname(__file__) # .py의 파일의 위치를 반환
image_path = os.path.join(current_path,"images") #이미지 폴더 위치 반환

# 배경
background = pygame.image.load(os.path.join(image_path,"background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2)-(character_width/2)
character_y_pos = screen_height-character_height-stage_height

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 5

# 무기
weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기 여러발 가능
weapons =[]

# 무기 이동 속도
weapon_speed = 10

# 공 만들기 (4개 크기에 대해 따로 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path,"balloon1.png")),
    pygame.image.load(os.path.join(image_path,"balloon2.png")),
    pygame.image.load(os.path.join(image_path,"balloon3.png")),
    pygame.image.load(os.path.join(image_path,"balloon4.png"))]

# 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9] 

# 공들
balls = []

# 최초 발생하는 큰 공 추가
balls.append({
    "pos_x" : 50, #공의 x 좌표
    "pos_y" : 50, #공의 y 좌표
    "img_idx" : 0,
    "to_x" : 3, #공의 x 축 이동방향
    "to_y" : -6,
    "init_spe_y" : ball_speed_y[0]}) #y의 최초속도


# Event Loop
running = True # Check whether game is running
while running:
    dt = clock.tick(30) #게임 화면의 초당 프레임 수 설정
#케릭터가 1초동안 100 만큼 이동하고 싶다
# 10 fps : 1초 동안에 10번 움직임 -> 1번에 10만큼 이동 10*10
# 20 fps : 1초 동안에 20번 움직임 -> 1번에 5만큼 이동 5*20

    #2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    #3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos <0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos  = screen_width-character_width

    # 무기 발사
    weapons = [[w[0],w[1]-weapon_speed] for w in weapons] #모든 무기 위치값에서  y 값이 변동하는

    # 천장에 닿은 무기 없애기
    weapons = [[w[0],w[1]] for w in weapons if w[1]>0 ]

    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls): #enumerate : balls 리스트에 있는 몇번 째 인덱스인지 그 벨류가 무엇인지 가져옴
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 가로 벽에 닿았을 때 공 이동 위치 변경
        if ball_pos_x < 0 or ball_pos_x > screen_width-ball_width:
            ball_val["to_x"] = ball_val["to_x"]* -1

        # 세로 위치
        # 스테이지에 튕겨서 올라가는 처리
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spe_y"]
        else: # 그 외의 모든 경우에는 속도 변경
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]
    #4. 충동처리
    
    #5. 화면에 그리기
    screen.blit(background, (0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x,ball_pos_y))

    screen.blit(stage, (0, screen_height-stage_height))
    screen.blit(character, (character_x_pos,character_y_pos))
    # 순선대로 그림을 그리기 때문에 제일 마지막이 제일 위에 그려짐
    

    pygame.display.update() # 게임화면을 지속적으로 매 프레임마다 그려내야하기 때문에 while 을 계속 돌리기 위한 코드

# 잠시대기
pygame.time.delay(2000) #2초 대기

# pygame End
pygame.quit()