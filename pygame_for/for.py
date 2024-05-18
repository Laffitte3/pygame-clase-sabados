import pygame

pygame.init()

ancho=800
largo=600


pantalla=pygame.display.set_mode((ancho,largo))


elmo=["frame-01.gif","frame-02.gif","frame-03.gif","frame-04.gif","frame-05.gif","frame-06.gif",
      "frame-07.gif","frame-08.gif","frame-09.gif","frame-10.gif","frame-11.gif","frame-12.gif",]


running = True
while running:


    for i in elmo:

        fondo=pygame.image.load(i)
        fondo=pygame.transform.scale(fondo,(ancho,largo))
        pygame.time.delay(40)
        pantalla.blit(fondo,(0,0))
        pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    


    pygame.display.update()