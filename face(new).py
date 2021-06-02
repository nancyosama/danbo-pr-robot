import pygame
import sys
import speech_recognition as sr
#sys gives us access to some  system commands

class Player(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load("a-11.png"))
        self.sprites.append(pygame.image.load("a-a.png"))
        self.sprites.append(pygame.image.load("a-b.png"))
        self.sprites.append(pygame.image.load("a-c.png"))
        self.sprites.append(pygame.image.load("a-d.png"))
        self.sprites.append(pygame.image.load("a-e.png"))
        self.sprites.append(pygame.image.load("a-f.png"))
        self.sprites.append(pygame.image.load("a-g.png"))
        self.sprites.append(pygame.image.load("a-h.png"))
        self.sprites.append(pygame.image.load("a-i.png"))
        self.sprites.append(pygame.image.load("a-j.png"))
        self.sprites.append(pygame.image.load("a-k.png"))
        self.sprites.append(pygame.image.load("a-i.png"))
        self.sprites.append(pygame.image.load("a-m.png"))
        self.sprites.append(pygame.image.load("a-n.png"))
        self.sprites.append(pygame.image.load("a-o.png"))
        self.sprites.append(pygame.image.load("a-p.png"))
        self.sprites.append(pygame.image.load("a-q.png"))
        self.sprites.append(pygame.image.load("a-r.png"))
        self.sprites.append(pygame.image.load("a-s.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [posx, posy]


    def update(self):
        self.current_sprite += 0.01
        if int(self.current_sprite) >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

    # we now have an image and then we need to draw rect around it
    # self.image= pygame.Surface([width,height]
    # self.image.fill(color)
    # self.rect = self.image.get_rect()


# till now our game has only one state

class GameState:
    x = 150
    y = 150
    w=10
    l=10
    def __init__(self):
        self.state = 'intro'

    def ons(self):
        screen.fill((0, 0, 0))
        cross_group.draw(screen)
        cross_group.update()

    def intro(self):
        #screen.fill((0, 0, 0))
        #cross_group.draw(screen)
        #cross_group.update()
        self.ons()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Drawing
                cross.rect.left -= 520
                print(cross)
            if event.type == pygame.MOUSEBUTTONUP:
                danb_sound.play()
                self.state = 's2t'
            if event.type == pygame.KEYDOWN:
                self.snd()
        pygame.display.flip()

    def snd(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        danb_sound.stop()
        self.ons()
        #cross.rect.right += 520
        # to make the display Surface actually appear on the user’s monitor.
        cross_group.update()

    def s2t(self):
        #gameDisplay.blit(gameDisplay, (0, 0))
        sound = "Driving-English-Conversation-Sample (online-audio-converter.com).wav"
        black = pygame.color.Color('#000000')
        white = pygame.color.Color('#ffffff')
        font = pygame.font.Font(None, 40)
        pygame.draw.rect(screen, white, (0, 0, self.w, self.l))
        text = font.render("hello world hello world hello jkglblguk hel hello world hello jkglblguk hel hello world hello jkglblguk helhello world hello jkglblguk hello world hello world", False, black)
        done = False
        while not done:
            screen.fill(white)
            screen.blit(text, (self.x, self.y))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
        pygame.quit()

        # we put our game into a method of this class

        # a method to organize which state to work

    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        # if self.state == 'main_game':
        # self.main_game()
        if self.state == 's2t':
            self.s2t()

            # text = r.recognize_google(audio)
            # print(text)

            # message_display(text)
# console setup
pygame.init()

# creating an object from the class
game_state = GameState()
danb_sound = pygame.mixer.Sound("Driving-English-Conversation-Sample (online-audio-converter.com).wav")
#gameDisplay = pygame.display.set_mode((100, 100))

width = 1200
length = 900
window_color = (0, 10, 50)

# build the window
screen = pygame.display.set_mode((width, length))  # width and height
pygame.display.set_caption("Danbo")
pygame.draw.rect(screen, window_color, (0, 0, 1000, 1000))



# to load an image and it wont be shown bec the background image is floating so we need to put this image in the
# background of thr screen image
# background = pygame.image.load("download.jpg")

# creating an object from the class
cross = Player(0, 0)

# it is a clock that calculates at what time
clock = pygame.time.Clock()

cross_group = pygame.sprite.Group()
cross_group.add(cross)
# gameDisplay = pygame.display.set_mode((500,500))
# sound1=pygame.mixer.Sound("sounds_bullet.wav")
# i want to switch between the states

while 1:
    game_state.state_manager()
    #it is the rate of each frame
    #this means that we are going to run this while loop 60 times each second
    clock.tick(70)



