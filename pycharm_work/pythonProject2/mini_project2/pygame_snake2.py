# 1. pygame 선언 및 사용할 패키지 임포트
import pygame
import random
from datetime import datetime
from datetime import timedelta

pygame.init() # pygame 초기화

# 2. pygame에 사용되는 전역변수 선언
size = [800, 600]
screen = pygame.display.set_mode(size)
# 창 타이틀 설정
pygame.display.set_caption("Catterpillar Game")

done = False
play = True
clock = pygame.time.Clock()
last_moved_time = datetime.now()



# 키 방향에 대한 딕셔너리 선언
KEY_DIRECTION = {
    pygame.K_UP: 'N',
    pygame.K_DOWN: 'S',
    pygame.K_LEFT: 'W',
    pygame.K_RIGHT: 'E',
}

# 배경화면 편집
SnakeLevel = (1)
SnakeLevel = str(SnakeLevel)
myfont = pygame.font.SysFont('DungGeunMo', 30)


# 3. 게임 구동에 필요한 함수와 클래스 선언

# 블럭을 그리기 위한 함수 선언
def draw_block(screen, color, position):
    block = pygame.Rect((position[1] * 20, position[0] * 20),  # 20을 곱하는 이유는 블록의 크기를 20픽셀로 설정
                        (20, 20))
    pygame.draw.rect(screen, color, block)


# 뱀에 관한 클래스 선언
class Snake:
    def __init__(self):
        self.positions = [(0, 2), (0, 1), (0, 0)]
        self.direction = ''
        self.head_image = pygame.image.load("image/catterpillar head.jpg").convert_alpha()
        self.head_image = pygame.transform.scale(self.head_image, (20, 20))
        self.body_images = [
            pygame.image.load("image/catterpillar_body_orange.png").convert_alpha(),
            pygame.image.load("image/catterpillar_body_sky.png").convert_alpha(),
            pygame.image.load("image/catterpillar_body_yellow.png").convert_alpha()
        ]
        self.body_images = [
            pygame.transform.scale(image, (20, 20)) for image in self.body_images
        ]
        self.block_size = 20

    def draw(self):
        # 머리 부분 그리기
        head_position = self.positions[0]
        head_angle = 0
        if self.direction == 'W':
            head_angle = 180
        elif self.direction == 'N':
            head_angle = 90
        elif self.direction == 'S':
            head_angle = 270
        head_image_rotated = self.rotate_image(self.head_image, head_angle)
        screen.blit(
            head_image_rotated,
            (head_position[1] * self.block_size, head_position[0] * self.block_size)
        )

        # 몸통 부분 그리기
        for i, position in enumerate(self.positions[1:-1]):
            if i >= len(self.body_images):
                # 새로 추가된 몸체이므로 랜덤한 이미지 선택
                body_image = random.choice(self.body_images)
                self.body_images.append(body_image)
            else:
                body_image = self.body_images[i]
            screen.blit(body_image, (position[1] * self.block_size, position[0] * self.block_size))

    def rotate_image(self, image, angle):
        rotated_image = pygame.transform.rotate(image, angle)
        return rotated_image

    def move(self):
        head_position = self.positions[0]
        y, x = head_position
        if self.direction == 'N':

            self.positions = [(y - 1, x)] + self.positions[:-1]
        elif self.direction == 'S':

            self.positions = [(y + 1, x)] + self.positions[:-1]
        elif self.direction == 'W':

            self.positions = [(y, x - 1)] + self.positions[:-1]
        elif self.direction == 'E':

            self.positions = [(y, x + 1)] + self.positions[:-1]


    def grow(self):
        tail_position = self.positions[-1]
        y, x = tail_position
        if self.direction == 'N':
            self.positions.append((y - 1, x))
        elif self.direction == 'S':
            self.positions.append((y + 1, x))
        elif self.direction == 'W':
            self.positions.append((y, x - 1))
        elif self.direction == 'E':
            self.positions.append((y, x + 1))



# 사과에 관한 클래스 선언
class Apple:
    def __init__(self, position=(9, 9)):
        self.position = position
        self.image = pygame.image.load("image/apple.jpg").convert_alpha()  # 이미지 로드
        self.image = pygame.transform.scale(self.image, (20, 20))

    def draw(self):
        screen.blit(self.image, (self.position[1] * 20, self.position[0] * 20))


# 4. pygame 무한루프(본체) 함수 선언
def runGame():
    global done, last_moved_time, text, SnakeLevel, play
    # 게임 시작 시, 뱀과 사과를 초기화
    snake = Snake()  # 뱀 클래스를 활용해 뱀 객체 1개 생성
    apple = Apple()  # 사과 클래스를 활용해 사과 객체 1개 생성
    speed = 0.1
    while not done:
        clock.tick(30)  # 초당 프레임 수

        if play == True:
            image = pygame.image.load('image\space.jpg')
            image = pygame.transform.scale(image, size)
            screen.blit(image, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    play = False
                if event.type == pygame.KEYDOWN:
                    if event.key in KEY_DIRECTION:
                        snake.direction = KEY_DIRECTION[event.key]

            if timedelta(seconds=speed) <= datetime.now() - last_moved_time:
                snake.move()
                last_moved_time = datetime.now()

            if snake.positions[0] == apple.position:
                snake.grow()
                speed -= speed/10
                apple.position = (random.randint(0, 19), random.randint(0, 19))
                text = myfont.render(SnakeLevel, False, (0, 0, 0))
                SnakeLevel = str(int(SnakeLevel) + 1)

            if snake.positions[0] in snake.positions[1:]:
                play = False

            head_position = snake.positions[0]
            if head_position[0] < 0 or head_position[0] >= 30 or head_position[1] < 0 or head_position[1] >= 40:
                play = False

            # frame 마다 업데이트
            snake.draw()
            apple.draw()
            text = myfont.render('Catterpillar Level : Lv.' + SnakeLevel, True, (000, 000, 000))
            screen.blit(text, (90, 10))
            pygame.display.update()

        else:
            image = pygame.image.load('image/gameover.jpg')
            image = pygame.transform.scale(image, size)
            screen.blit(image, (0, 0))
            text = myfont.render('David\'s Catterpillar Game', True, (255, 255, 255))
            screen.blit(text, (90, 30))

            text = myfont.render('   Your Highest Lv.' + SnakeLevel, True, (255, 255, 255))
            screen.blit(text, (90, 60))

            text = myfont.render('If you want to restart, Press spacebar', True, (255, 255, 255))
            screen.blit(text, (400, 500))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        play = True
                        snake = Snake()  # 뱀 클래스를 활용해 뱀 객체 새롭게 1개 생성
                        apple = Apple()  # 사과 클래스를 활용해 사과 새롭게 객체 1개 생성
                        SnakeLevel = str(int(1))  # 스네이크 레벨 초기화
                        speed = 0.1

        pygame.display.update()


# 5. 전체 프로그램 돌리기

runGame()
pygame.quit()