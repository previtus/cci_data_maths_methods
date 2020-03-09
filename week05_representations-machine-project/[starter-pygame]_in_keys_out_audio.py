# Setup:
# follow https://www.pygame.org/wiki/GettingStarted ( python3 -m pip install -U pygame --user )

import pygame

play_output = "kick.wav"

possible_outputs = ["closed_hi_hat.wav", "kick.wav", "open_hi_hat.wav", "snare.wav"]


pygame.init()
pygame.mixer.init()
pygame.display.set_caption(u'Keyboard events')
pygame.display.set_mode((400, 400))

while True:
    # gets a single event from the event queue
    event = pygame.event.wait()
    # if the 'close' button of the window is pressed
    if event.type == pygame.QUIT:
        # stops the application
        break

    # captures the 'KEYDOWN' events
    if event.type == pygame.KEYDOWN:
        key_name = pygame.key.name(event.key)
        key_name = key_name.upper()

        print(u'"{}" key pressed'.format(key_name))
        # Do something with the state of your machine ...

        if key_name == "LEFT":
            play_output = possible_outputs[0]

        if key_name == "RIGHT":
            play_output = possible_outputs[1]


    pygame.mixer.music.load(play_output)
    pygame.mixer.music.play()



pygame.quit()
