import pygame

# Definindo as constantes de cores com o sistema RGB
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
ROXO = (137, 0, 255)
AMARELO = (255, 255, 0)
CIANO = (0, 255, 255)

# Definindo pi
PI = 3.1416

# inicializamos os módulos de Pygame
pygame.init()


janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Roblox RXT ON")

janela.fill(PRETO)

pygame.display.update()

# Adicionando o texto
# fonte com arquivo: font_path = "Arquivo.ttf"
fonte = pygame.font.SysFont("Monocraft" ,48)
# Utilizando o método render() para renderizar o texto
texto = fonte.render('Mine', True, VERDE, None)
janela.blit(texto, [30, 150])
texto = fonte.render('cré', True, AZUL, None)
# Desenha o conteudo na tela
janela.blit(texto, [160, 150])


pygame.draw.line(janela, VERDE, [60,260], [420,260], 4) # Nessa ordem é o inicio da linha, o final da linha e a grossura dela
pygame.draw.polygon(janela, AZUL, ([191,206], [236,277], [156,277]), 0) # Janela, cor, Coordenadas do vértices, Largura da linha
pygame.draw.circle(janela, VERMELHO, (300,500),20,0)# Coordenadas do centro, Raio do circulo em pixels, Largura da linha, [Horizontal, Vertical]
pygame.draw.ellipse(janela, BRANCO, (400, 250, 40, 80), 100) # ((Esquerda, Topo, Largura, Altura), Largura da linha)
pygame.draw.rect(janela, ROXO, (20,20,60,40),0) # ((Esquerda, Topo, Largura, Altura), Largura da linha)
pygame.draw.arc(janela, AMARELO, (250,75,250,125), PI / 2, 3 * PI, 2) # (Janela, Cor, Coordenadas (Esquerda, Topo, Largura, Altura), Ângulo inicial, Ângulo final, Largura da Linha)
pygame.draw.arc(janela, CIANO, (250,75,250,125), - PI / 2, 3 / PI, 2)
pygame.display.update()
deve_continuar = True

while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False
pygame.quit()