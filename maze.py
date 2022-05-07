#создай игру "Лабиринт"!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, widit, height, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (widit, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.step = player_speed


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Pleyer(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.step
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.step
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.step
        if keys[K_d] and self.rect.x < 600:
            self.rect.x += self.step
        

class Enemy(GameSprite):
    def __init__(self, player_image, widit, height, player_x, player_y, player_speed):
        super().__init__(player_image, widit, height, player_x, player_y, player_speed)
        self.direction = 'left'

    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.step
            if self.rect.x <= 450:
                self.direction = 'right'
        else:
            self.rect.x += self.step
            if self.rect.x >= 580:
                self.direction = 'left'
            
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wight, height, x_pos, y_pos):
        super().__init__()
        self.color = (color_1, color_2, color_3)
        self.image = Surface((wight, height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
    
    def drow_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

FPS = 60

wall_3 = Wall(0, 255, 0, 700, 5, 0, 0)
wall_4 = Wall(0, 255, 0, 10, 370, 230, 0)
wall_5 = Wall(0, 255, 0, 10, 500, 350, 150)
wall_6 = Wall(0, 255, 0, 250, 10, 350, 150)


mixer.init()
clock = time.Clock()
game = True
window = display.set_mode((700,500))
display.set_caption('Лабиринт')
background = GameSprite('background.jpg',700,500,0,0,0)
mixer.music.load('jungles.ogg')
mixer.music.play()
hero = Pleyer('hero.png', 100, 100 , 100, 300, 10)
enemy = Enemy('cyborg.png', 100,100, 580, 230, 3)
finish = False
font.init()
font = font.Font(None, 70)
lose = font.render('Ты проиграл!', True, (250, 0,0))
win = font.render('Ты победил!', True, (0, 250,0))
kick = mixer.Sound('kick.ogg')
mone = mixer.Sound('money.ogg')
texsture = GameSprite('treasure.png', 80,80,550,400,0)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False   ладно ладно бб
    if not finish:
        hero.update()
        enemy.update()       как сделать выход из игры на кнопку на клавишу
        background.reset()
        
        wall_3.drow_wall()     
        wall_4.drow_wall()         
        wall_5.drow_wall()    
        wall_6.drow_wall()    
         
        texsture.reset()
        hero.reset()
        enemy.reset()
        if  sprite.collide_rect(hero, enemy) or sprite.collide_rect(hero, wall_3) or sprite.collide_rect(hero, wall_4) or sprite.collide_rect(hero, wall_5) or sprite.collide_rect(hero, wall_6):
            finish = True
            window.blit(lose, (200,200))
            kick.play()
        if sprite.collide_rect(hero, texsture):
            finish = True   
            window.blit(win, (200,200))
            mone.play()
    display.update()
    clock.tick(FPS)

