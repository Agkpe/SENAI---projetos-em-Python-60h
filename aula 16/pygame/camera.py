import pygame


pygame.init()
tamanho  =  300,150
screen = pygame.display.set_mode(tamanho)


run = True
while run:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
         screen.fill('LightSkyBlue')
         
         pygame.draw.rect(screen,'black',(125,50,50,50) ) 
         pygame.draw.circle(screen,'pink',(50,50), 50 ) 
         pygame.draw.line(screen, 'green', (200,200), (50,50), 5)
         pygame.draw.ellipse(screen, 'red', (170,30,150,40))


         pygame.display.update()
         
pygame.quit()               
         
         
    


  



