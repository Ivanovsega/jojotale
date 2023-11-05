#Создай собственный Шутер!
from random import randint
from pygame import *
from tkinter.font import Font
mixer.init()
mixer.music.load('spamton.ogg')
mixer.music.play()
fire_sound = mixer.Sound('awp1.ogg')
#tkinter.font.ITALIC
font.init()

font1 = font.SysFont('Papyrus', 80)
win = font1.render('Shinzou wo sasageyo', True, (250, 250 , 250))
lose = font1.render('Wasteg', True, (250, 250 , 250))

font2 = font.SysFont("Papyrus", 36)

img_back = "deep_dark_fone.png"
img_enemy = "spam.png"
img_enemy2 = "jevil.png"
img_hero = "nice.jpg"
img_hero2 = "queen.png"
img_bullet = "hearts.jpg"
img_bullet2 = "hearts.jpg"
score = 0
lost = 0
max_lost = 99999
goal = 993

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.speed = player_speed
        self.image = transform.scale(image.load(player_image), (size_x, size_y))

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        #if keys[K_UP] and self.rect.y > 5:
            #self.rect.y -= self.speed
        #if keys[K_DOWN] and self.rect.y < win_width - 80:
            #self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        #if keys[K_w] and self.rect.y > 5:
            #self.rect.y -= self.speed
        #if keys[K_s] and self.rect.y < win_width - 80:
            #self.rect.y += self.speed  
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx + 30, self.rect.top, 25, 25, -1)
        bullets.add(bullet)
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 25, 25, -2)
        bullets.add(bullet)
        bullet = Bullet(img_bullet, self.rect.centerx - 30, self.rect.top, 25, 25, -3)
        bullets.add(bullet)
     
    def fire2(self):
        bullet = Bullet(img_bullet2, self.rect.centerx - 20, self.rect.top, 25, 25, -2)
        bullets.add(bullet)  
        bullet = Bullet(img_bullet2, self.rect.centerx + 20, self.rect.top, 25, 25, -2)
        bullets.add(bullet) 



class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1 



class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

win_width = 1000
win_height = 700
win_height2 = 250
display.set_caption("Jojotale")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
ship = Player(img_hero, 5, win_height - 100, 80, 100, 15)
ship2 = Player(img_hero2, 100, win_height - 100, 100, 100, 15)

monsters = sprite.Group()
bullets = sprite.Group()

for i in range(1, 6):
    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 3))
    monsters.add(monster)
for i in range(1, 6):
    monster2 = Enemy(img_enemy2, randint(80, win_width - 80), -40, 80, 50, randint(1, 3))
    monsters.add(monster2)



#обработай событие «клик по кнопке "Закрыть окно"»

game = True
finish = False
fps = 31
ddd = True



#docs.google.com/document/1eH5u5SAaiqXRIeEXrSW93p3z0BQcR72vjTweP4v0wNw/edit
f1 = False
f2 = False

while ddd:
    for e in event.get():
        if e.type == QUIT:
            ddd = False

        elif e.type == KEYDOWN:
            if e.key == K_w:
                fire_sound.play()
                f1 = True
            if e.key == K_UP:
                fire_sound.play()
                f2 = True
        elif e.type == KEYUP:
            if e.key == K_w:
                fire_sound.play()
                f1 = False
            if e.key == K_UP:
                fire_sound.play()
                f2 = False   
    if f1:
        ship.fire()
    if f2:
        ship2.fire2()
    if not finish:
        window.blit(background,(0,0))
        ship.update()
        ship.reset()
        ship2.update2()
        ship2.reset()
        monsters.update()
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)

        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score = score + 1
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80 ,50, randint(1, 3))
            monsters.add(monster)
        for c in collides:
            score = score + 1
            monster2 = Enemy(img_enemy2, randint(80, win_width - 80), -40, 80 ,50, randint(1, 3))
            monsters.add(monster2)
        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True
            window.blit(lose, (200, 200))
        if sprite.spritecollide(ship2, monsters, False) or lost >= max_lost:
            finish = True
            window.blit(lose, (200, 200))
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))

        text = font2.render("Destroyed:" + str(score), 1, (240, 120, 40))
        window.blit(text, (10,20))
        text_lose = font2.render("Missed:" + str(lost), 1,(240, 120 , 40))
        window.blit(text_lose, (10,50)) #pygame.


        display.update()

    else:
        finish = False
        score = 0
        lost = 0
        for b in bullets:
            b.kill()
        for m in monsters:
            m.kill()
        time.delay(1500)
        for i in range(1, 6):
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 3))
            monsters.add(monster)
        for i in range(1, 9):
            monster2 = Enemy(img_enemy2, randint(80, win_width - 80), -40, 80, 50, randint(1, 3))
            monsters.add(monster2)
time.delay(11)
    #clock.tick(fps)