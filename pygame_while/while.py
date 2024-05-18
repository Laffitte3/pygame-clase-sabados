import pygame

pygame.init()

ancho=800
largo=600

FPS=60
reloj=pygame.time.Clock()

pantalla=pygame.display.set_mode((ancho,largo))

dragon_image=pygame.image.load("dragon_right.png")
dragon_rect=dragon_image.get_rect()
dragon_rect.topleft=(32,largo/2)

espacios_recorridos=3
running = True
while running:

    keys=pygame.key.get_pressed()

    """if keys[pygame.K_RIGHT] and dragon_rect.right<ancho-100:
            dragon_rect.x +=espacios_recorridos
            print(dragon_rect.x)"""
        
    #Espacios recorridos tiene el valor de 3
    dragon_rect.x +=espacios_recorridos
    print(dragon_rect.x)


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    pantalla.fill((50,0,50))
    pantalla.blit(dragon_image,dragon_rect)





    pygame.draw.line(pantalla,(255,255,255),(ancho-64,0),(ancho-64,largo),2)


    pygame.display.update()
    reloj.tick(FPS)