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

    #3. 게임 캐릭터 위치 정의


    #4. 충동처리
    
    #5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(stage, (0, screen_height-stage_height))
    screen.blit(character, (character_x_pos,character_y_pos))
    pygame.display.update() # 게임화면을 지속적으로 매 프레임마다 그려내야하기 때문에 while 을 계속 돌리기 위한 코드

# 잠시대기
pygame.time.delay(2000) #2초 대기

# pygame End
pygame.quit()