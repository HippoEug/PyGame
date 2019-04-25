import pygame # Import pygame module

x = 0
y = 440
width = 40
height = 60

velocity = 10

pygame.init() # Init pygame
win = pygame.display.set_mode((500, 500)) # Set display size to 500x500 pixels
pygame.display.set_caption("First Game") # Set application name

isJumping = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(50) # Game refresh rate at 50ms

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed() # Get keyboard input
    if ((keys[pygame.K_LEFT] or keys[pygame.K_a]) and x > 0): # If A or Left is pressed
        x = x - velocity
    if ((keys[pygame.K_RIGHT] or keys[pygame.K_d]) and x < (500 - width)): # If D or Right is pressed
        x = x + velocity

    if not (isJumping): # If not jumping
        if ((keys[pygame.K_UP] or keys[pygame.K_w]) and y > 0):
            y = y - velocity
        if ((keys[pygame.K_DOWN] or keys[pygame.K_s]) and y < (500 - height)):
            y = y + velocity
            
        if keys[pygame.K_SPACE]:
            isJumping = True
    else: # If space bar is hit, isJumping is set
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y = y - ((jumpCount ** 2)/2)*neg
            jumpCount = jumpCount - 1
        else:
            isJumping = False # Reset isJumping state back to False
            jumpCount = 10 # Rest jumpCount value

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) # Draw rect with params ((rgb), (coords))
    pygame.display.update()

pygame.quit()
