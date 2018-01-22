import pygame, pygame.mixer, random, time, codecs

path = 'D://PythonPrograms//AsteroidPackage//highscores.txt'
hs_file = open(path, 'r')
hs = hs_file.read()
hs_file.close()

pygame.init()
pygame.mixer.init()

display_width = 1800
display_height = 800
name = "Asteroid"
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
red = (255, 0, 0)
green = (0, 255, 0)
new_score = 0
life = 3
colors = [white, red, blue, green]
gameFPS = 75
introFPS = 15
y = 0
x = 0

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Astroid")
clock = pygame.time.Clock()


shipImg = pygame.image.load("ship.png")
shipImg = pygame.transform.scale(shipImg,(50, 25))
background = pygame.image.load("space.png")
background = pygame.transform.scale(background, (display_width, display_height))
ast = pygame.image.load("asteroid.png")
ast = pygame.transform.scale(ast, (75, 75))
play_button = pygame.image.load("play_button.png")
play_button = pygame.transform.scale(play_button, (200, 85))
quit_button = pygame.image.load("quit_button.png")
quit_button = pygame.transform.scale(quit_button, (85, 85))
fail = pygame.mixer.Sound("failure.wav")




class asteroid:
    def __init__(self, startx, starty, speedy):
        self.startx = startx
        self.starty = starty
        self.speedy = speedy
    
    def asteroid_draw(self):
        global new_score
        global x
        global y

        screen.blit(ast, (self.startx, self.starty))
        self.starty += self.speedy
        if self.starty > display_height:
            self.starty = -50
            self.startx = random.randrange(0, display_width -100)
            new_score += 1
            self.speedy += 1
        if y + 15 < self.starty + 69 and y + 13 > self.starty:
            if (x + 20 > self.startx and x + 20 < self.startx + 69 or x + 30 > self.startx and x + 30 < self.startx + 69):
                crash(new_score)
        
def game_music():
    pygame.mixer.music.load("game.wav")
    pygame.mixer.music.play(-1)

def display_score(count):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Score: " + str(count), True, white)
    screen.blit(text, (1070,0))

def ship(x,y):
    screen.blit(shipImg, (x,y))

def space():
    screen.blit(background, (0,0))

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def message_display(text):
    text_font = pygame.font.SysFont(None, 110)
    TextSurf, TextRect = text_objects(text, text_font)
    TextRect.center = ((display_width/2, display_height/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    global new_score
    new_score = 0
    game_intro()


def crash(new_score):
    global hs
    global path
    path = 'D://PythonPrograms//AsteroidPackage//highscores.txt'
    pygame.mixer.music.stop()
    space()
    fail.play()
    if new_score > int(hs):
        new_hs_file = open(path, 'w')
        new_hs_file.write(str(new_score))
        new_hs_file.close()
        file = open(path, 'r')
        hs = file.read()
        file.close()
    message_display("Game over! Score: " + str(new_score))


def button(image, x, y, w, h, color, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if click[0] == 1 and action != None:
            action()
    screen.blit(image, (x, y))

def quitgame():
    pygame.quit()
    quit()
    

def game_intro():
    intro = True
    global new_score
    game_music()
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        space()
        font = pygame.font.SysFont(None, 140)
        title = font.render("ASTEROID", True, white)
        screen.blit(title, (700, 175))
        small = pygame.font.SysFont(None, 25)
        text = small.render("Use WASD and Arrow Keys to control the ships.", True, white)
        text1 = small.render("Avoid crashing!", True, white)
        medium = pygame.font.SysFont(None, 35)
        high = medium.render("All Time Highscore: " + hs, True, white)
        smaller = pygame.font.SysFont(None, 20)
        credit = smaller.render("Created by Andrew Rawlings - DEC 10, 2017 - Version 1.0", True, white)
        screen.blit(credit, (0,display_height - 20))
        screen.blit(text, (700, 350))
        screen.blit(text1, (700, 380))
        screen.blit(high, (700, 300))
        button(play_button, 200, 300, 200, 85, blue, game_loop)
        button(quit_button, 255, 400, 85, 85, red, quitgame)
        pygame.display.update()
        clock.tick(introFPS)

    

def game_loop():
    global new_score
    global y
    global x
    x = (display_width * .45)
    y = (display_height * .55)
    x_change = 0
    y_change = 0
    new_score = 0
    asteroid1 = asteroid((random.randrange(0, display_width-100)), -100, 2)
    asteroid2 = asteroid((random.randrange(0, display_width-100)), -100, 3)
    asteroid3 = asteroid((random.randrange(0, display_width-100)), -100, 4)
    asteroid4 = asteroid((random.randrange(0, display_width-100)), -100, 5)
    asteroid5 = asteroid((random.randrange(0, display_width-100)), -100, 6)
    asteroid6 = asteroid((random.randrange(0, display_width-100)), -100, 7)
    asteroid7 = asteroid((random.randrange(0, display_width-100)), -100, 8)
        
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -10
                elif event.key == pygame.K_d:
                    x_change = 10
                elif event.key == pygame.K_w:
                    y_change = -10
                elif event.key == pygame.K_s:
                    y_change = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0

        x += x_change
        y += y_change
        
        
        space()
        
        asteroid1.asteroid_draw()
        asteroid2.asteroid_draw()
        asteroid3.asteroid_draw()
        asteroid4.asteroid_draw()
        asteroid5.asteroid_draw()
        asteroid6.asteroid_draw()
        asteroid7.asteroid_draw()
        
        ship(x,y)
        
        if x > display_width - 45 or x < 0:
            crash(new_score)
        if y < 0 or y > display_height - 20:
            crash(new_score)
            
        display_score(new_score)
        pygame.display.update()

        clock.tick(gameFPS)

game_music()
game_intro()
game_loop()
pygame.quit()
quit()
                

    
