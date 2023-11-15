# Pantalla de inicio
def show_go_screen():
    # Inicializamos la posición vertical del fondo
    bg_y = 0
    # Variable que indica si estamos esperando una acción del jugador
    waiting = True
    # Bucle principal de la pantalla de inicio
    while waiting:
        # Manejamos los eventos de pygame
        for event in pygame.event.get():
            # Si el evento es cerrar la ventana, salimos del juego
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Si el evento es soltar una tecla, dejamos de esperar
            if event.type == pygame.KEYUP:
                waiting = False
        # Movemos el fondo hacia abajo
        bg_y += 1
        # Si el fondo ha pasado la altura de la pantalla, lo reiniciamos
        if bg_y > HEIGHT:
            bg_y = 0
        # Mostramos el fondo en dos posiciones para crear un efecto de movimiento
        screen.blit(background, (0, bg_y - HEIGHT))
        screen.blit(background, (0, bg_y))
        # Mostramos varios textos en la pantalla de inicio
        draw_text(screen, "U. SALESIANA", 65, WIDTH // 2, HEIGHT // 4)
        draw_text(screen, "Ingenieria de Sistemas", 27, WIDTH // 2, HEIGHT // 2)
        draw_text(screen, "InnoCoders", 20, WIDTH // 2, HEIGHT // 2 + 40)
        draw_text(screen, "Enter Para Jugar", 20, WIDTH // 2, HEIGHT * 3/4)
        # Actualizamos la pantalla
        pygame.display.flip()
        # Establecemos el límite de fotogramas por segundo a 60
        clock.tick(60)
