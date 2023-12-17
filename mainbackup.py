

# import the pygame module, so you can use it
import os
import pygame

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
APPLICATION_NAME = "Password Plus"
 
# define a main function
def main():
    # Change the working directory to the place where this .py file is located so that relative paths will work
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load(os.path.join('assets', 'Logo32x32.png'))
    pygame.display.set_icon(logo)
    pygame.display.set_caption(APPLICATION_NAME)
     
    # create a surface on screen that has the size
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    # load set graphic
    set_image = pygame.image.load(os.path.join('assets', 'Set.png')).convert()
 
    # Using blit to copy content from one surface to other
    screen.blit(set_image, (0, 0))

    # update the display
    pygame.display.flip()

    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()