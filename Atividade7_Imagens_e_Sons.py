import pygame, random

# Carregando imagens
imagemGastly = pygame.image.load("img/gastly.png")
imagemCandy = pygame.image.load("img/rarecandy.png")
imagemFundo = pygame.image.load("img/lavandertown.png")

# # definindo as cores
# PRETO = (0, 0, 0)
# VERDE = (0, 255, 0)
# BRANCO = (255, 255, 255)

# definindo outras constantes do jogo
LARGURAJANELA = 1920
ALTURAJANELA = 1080
VEL = 6
ITERACOES = 30
TAMANHOBLOCO = 20
LARGURACANDY = 45
ALTURACANDY = 45
LARGURAGASTLY = 120
ALTURAGASTLY = 120

# Redimensionando as imagens
imagemFundo = pygame.transform.scale(imagemFundo, (LARGURAJANELA, ALTURAJANELA))
imagemCandy = pygame.transform.scale(imagemCandy, (LARGURACANDY, ALTURACANDY))
imagemGastly = pygame.transform.scale(imagemGastly, (LARGURAGASTLY, ALTURAGASTLY))

# definindo a função moverJogador(), que registra a posição do jogador
def moverJogador(jogador, teclas, dimensaoJanela):
    bordaEsquerda = 0
    bordaSuperior = 0
    bordeDireita = dimensaoJanela[0]
    bordaInferior = dimensaoJanela[1]
    if teclas["esquerda"] and jogador["objRect"].left > bordaEsquerda:
        jogador["objRect"].x -= jogador["vel"]
    if teclas["direita"] and jogador["objRect"].right < bordeDireita:
        jogador["objRect"].x += jogador["vel"]
    if teclas["cima"] and jogador["objRect"].top > bordaSuperior:
        jogador["objRect"].y -= jogador["vel"]
    if teclas["baixo"] and jogador["objRect"].bottom < bordaInferior:
        jogador["objRect"].y += jogador["vel"]

# definindo a função moverBloco(), que registra a posição do bloco
def movercandy(candy):
    candy["objRect"].x += candy["vel"]

# inicializando pygame
pygame.init()

# instanciando método Clock para variavel relogio
relogio = pygame.time.Clock()

# criando janela
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption("Imagen e som")

# criando jogador
jogador = {
    "objRect": pygame.Rect(300, 100, LARGURAGASTLY, ALTURAGASTLY),
    "imagem": imagemGastly,
    "vel": VEL,
    "colisaoRect": pygame.Rect(300 + 50, 100 + 50, LARGURAGASTLY - 100, ALTURAGASTLY - 100)
}

# Configurando som
somComer = pygame.mixer.Sound("mp3/Gastly.mp3")

# Carregar musica de fundo
pygame.mixer.music.load("mp3/SomDeFundo.mp3")

# Definir o volume (Por exemplo, 0.1 para 10% do volume máximo)
pygame.mixer.music.set_volume(1.1)

# Reproduzir a música em loop
pygame.mixer.music.play(-1, 0.0)

somAtivado = True
# definindo o dicionario que guardará as direcoes pressionadas
teclas = {"esquerda": False, "direita": False, "cima": False, "baixo": False}

# inicializando outras variáveis
contador = 0
candys = []
deve_continuar = True

# loop do jogo
while deve_continuar:
    # checando os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_ESCAPE:
            deve_continuar = False
        if evento.key == pygame.K_m:
            if somAtivado:
                pygame.mixer.music.stop()
                somAtivado = False
        else:
            pygame.mixer.music.play(-1, 0.0)
            somAtivado = True

    # quando um botao do mouse é pressionado
    if evento.type == pygame.MOUSEBUTTONDOWN:
        candys.append({"objRect": pygame.Rect(evento.pos[0], evento.pos[1], LARGURACANDY, ALTURACANDY), "imagem": imagemCandy, "vel": VEL - 3})
    
    # Verifique o estado atual das teclas
    teclas = pygame.key.get_pressed()
    teclas = {
        "esquerda": teclas[pygame.K_LEFT] or teclas[pygame.K_a],
        "direita": teclas[pygame.K_RIGHT] or teclas[pygame.K_d],
        "cima": teclas[pygame.K_UP] or teclas[pygame.K_w],
        "baixo": teclas[pygame.K_DOWN] or teclas[pygame.K_s],
    }

    contador += 1
    if contador >= ITERACOES:
        contador = 0
        posY = random.randint(0, (LARGURAJANELA - ALTURACANDY))
        posX = -LARGURACANDY
        velRandom = random.randint(VEL - 3, VEL + 3)
        candys.append({"objRect": pygame.Rect(posX, posY, LARGURACANDY, ALTURACANDY), "imagem": imagemCandy, "vel": velRandom})

    # preenchendo o fundo de janela com a cor preta
    janela.blit(imagemFundo, (0, 0))

    # movendo o jogador
    moverJogador(jogador, teclas, (LARGURAJANELA, ALTURAJANELA))

    # desenhando jogador
    janela.blit(jogador["imagem"], jogador["objRect"])

    # checando se jogador bateu em algum bloco ou se bloco saiu da janela para retirá-lo da lista
    for candy in candys:
        comeu = jogador["objRect"].colliderect(candy["objRect"])
        if comeu and somAtivado:
            somComer.play()
        if comeu or candy["objRect"].x > ALTURAJANELA:
            candys.remove(candy)

    # Não esqueça de atualizar a posição do rect de colisão a cada movimento do jogador
    jogador["colisaoRect"].topleft = (jogador["objRect"].x + 50, jogador["objRect"].y + 50)

    # movendo e desenhando os blocos
    for candy in candys:
        movercandy(candy)
        janela.blit(candy["imagem"], candy["objRect"])

    # atualizando a janela
    pygame.display.update()

    # FPS
    relogio.tick(60)
  
# encerrando módulos de Pygame
pygame.quit()      