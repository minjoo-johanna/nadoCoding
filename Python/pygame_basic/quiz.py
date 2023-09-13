"""
Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

[게임 조건]
1. 케릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
3. 캐릭터가 동을 피하면 다음 똥이 다시 떨어짐
4. 캐릭터가 똥과 충돌하면 게임 종료
5. FPS 는 30으로 고정

[게임 이미지]
1. 배경 : 640 * 480 (세로 가로) - background.png
2. 캐릭터 : 70 * 70 - character.png
3. 똥 : 70 * 70 - enemy.png
"""

import pygame
import random
############################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height= 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("게임 이름")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("/Users/minjookim/BX23/CS_extra/nadoCoding/pygame_basic/pygame_basic/background.jpeg")

# 캐릭터 이미지 불러오기
character = pygame.image.load("/Users/minjookim/BX23/CS_extra/nadoCoding/pygame_basic/pygame_basic/character.jpeg")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가자 아래에
to_x = 0
character_speed = 10

# 적 enemy 캐릭터
enemy = pygame.image.load("/Users/minjookim/BX23/CS_extra/nadoCoding/pygame_basic/pygame_basic/enemy.jpeg")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = random.randint(0, screen_width - enemy_width) # 화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos = 0 # 화면 세로 크기 가자 아래에
enemy_speed = 10

############################################################

# 1. 사용자 게임 초기화 (배경 화면,게임 이미지, 좌표, 속도, 폰트 등)
  
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정
   
    # 2. 이벤트 처리 (키보드, 마우스 등)
    print("fps : " + str(clock.get_fps()))
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가? 
            running = False

    if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_LEFT:
            to_x -= character_speed
        if event.key == pygame.K_RIGHT:
            to_x += character_speed
    
    if event.type == pygame.KEYUP:
        x_to = 0
           
    
    # 3. 게임 케릭터 위치 정의
    character_x_pos += to_x * dt
    
    # 가로 경계값 처리
    if character_x_pos < 0: # 화면 이탈
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    enemy_y_pos += enemy_speed
    
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
        
    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    # 충돌 체크
    if character_rect.colliderect(enemy_rect): 
        print("충돌했어요")
        running = False
    
    # 5. 화면에 그리기
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

    pygame.display.update() # 게임화면을 다시 그리기!
    
# pygame 종료
pygame.quit(  )
