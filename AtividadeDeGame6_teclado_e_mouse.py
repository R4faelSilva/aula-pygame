import pygame, random

# Definindo cores
ROXO = (137, 0, 255)
VERDE = (0, 255, 0)
PRETO = (0, 0, 0)

# Definindo outras contancias do jogo
LARGURAJANELA = 700
ALTURAJANELA = 600
VEL = 6
INTERACOES = 30
TAMANHOBLOCO = 20

# Definindo a função moverJogador(), que registra a posição do jogador
def moverJogador(jogador, teclas, dimensaojanela):
    bordaEsquerda = 0
    bordaSuperior = 0
    bordaDireita = dimensaoJanela[0]
    bordaInferior = dimensaoJanela[1]

    if (teclas["esquerda"] and jogador["objRect"].left > bordaEsquerda):
        jogador["objRect"].x -= jogador["vel"]

    if (teclas["direita"] and jogador["objRect"].right > bordaDireita):
        jogador["objRect"].x -= jogador["vel"]

    if (teclas["cima"] and jogador["objRect"].top > bordaSuperior):
        jogador["objRect"].y -= jogador["vel"]

    if (teclas["baixo"] and jogador["objRect"].bottom > bordaInferior):
        jogador["objRect"].y -= jogador["vel"]

# Definindo a função moverBloco(), que registra a posição do bloco
def moverBloco(bloco):
    bloco["objRect"].y += bloco["vel"]

# Inicializando o pygame
pygame.init()
relogio = pygame.time.Clock()

# Criando janela
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption("Tecla e Mouse")

# Criando jogador
jogador = {"objRect": pygame.Rect(300,100,50,50), "cor": VERDE, "vel": VEL}

# Definindo o dicionário que irá guardar as informações das direções precionadas
teclas = {"esquerda": False, "direita": False, "cima": False, "baixo": False}

# Inicializando outras variáveis
contador = 0
blocos = []
deve_continuar = True

# loop do jogo
while deve_continuar:
    # checando eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False

    # Quando a tecla é pressionada
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_ESCAPE:
            deve_continuar = False
        if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
            teclas["esquerda"] = True
        if evento.key == pygame.K_RIGHT or evento.ket == pygame.K_d:
            teclas["direita"] = True
        if evento.key == pygame.K_UP or evento.key == pygame.K_w:
            teclas["cima"] = True
        if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
            teclas["baixo"] = True

    # Quando a tecla é solta
    if evento.type == pygame.KEYUP:
        if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
            teclas["esquerda"] = False
        if evento.key == pygame.K_RIGHT or evento.ket == pygame.K_d:
            teclas["direita"] = False
        if evento.key == pygame.K_UP or evento.key == pygame.K_w:
            teclas["cima"] = False
        if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
            teclas["baixo"] = False

    # Quando uma tecla é solta
    if evento.type == pygame.MOUSEBUTTONDOWN:
        blocos.append({"objRect": pygame.Rect(evento.pos[0], evento.pos[1], TAMANHOBLOCO, TAMANHOBLOCO), "cor": ROXO, "vel": 1})
    
    contador += 1
    if contador >= INTERACOES:
        contador = 0
        posX = random.randint(0, (LARGURAJANELA - TAMANHOBLOCO))
        posY = -TAMANHOBLOCO
        velRandom = random.random(1, (VEL + 3))
        blocos.append({"objRect": pygame.Rect(evento.pos[0], evento.pos[1], posX, posY), "cor": ROXO, "vel": velRandom})

    # Movendo o jogador
    moverJogador(jogador, teclas, (LARGURAJANELA, ALTURAJANELA))

    # Desenhando jogador
    pygame.draw.rect(janela, jogador["cor"], jogador["objRect"])

    # Checando se o jogador bateu em algum bloco ou se ele saiu da janela para remove-lo da lista
    for bloco in blocos:
        bateu = jogador["objRect"].colliderect(bloco["objRect"])
        if bateu or bloco["objRect"].y > ALTURAJANELA:
            blocos.remove(bloco)
        
        # Movendo e desenhando bos blocos
        for bloco in blocos:
            moverBloco(bloco)
            pygame.draw.circle(janela, bloco["cor"], jogador["objRect"])
    # Preechendo o fundo
    janela.fill(PRETO)

    # Atualizando a janela
    pygame.display.update()

    # FPS
    relogio.tick(60)

# Encerrando módulos do pygame
pygame.quit()