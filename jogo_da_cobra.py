import tkinter as tk
from tkinter import messagebox

# Configurações do campo e direções
LARGURA_CAMPO = 400
ALTURA_CAMPO = 200
TAMANHO_BLOCO = 20
DIREITA = (1, 0)
ESQUERDA = (-1, 0)
CIMA = (0, -1)
BAIXO = (0, 1)

class JogoMinhoca:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Minhoca")
        self.canvas = tk.Canvas(root, width=LARGURA_CAMPO, height=ALTURA_CAMPO, bg="black")
        self.canvas.pack()

        # Inicializando a posição e direção
        self.x = LARGURA_CAMPO // 2
        self.y = ALTURA_CAMPO // 2
        self.direcao = DIREITA

        # Criando a minhoca como um retângulo
        self.minhoca = self.canvas.create_rectangle(self.x, self.y, self.x + TAMANHO_BLOCO, self.y + TAMANHO_BLOCO, fill="green")

        # Vinculando as teclas para movimentação
        self.root.bind("<KeyPress>", self.capturar_tecla)

        # Iniciando o loop de movimentação
        self.movimento()

    def movimento(self):
        # Atualiza a posição da minhoca
        self.x += self.direcao[0] * TAMANHO_BLOCO
        self.y += self.direcao[1] * TAMANHO_BLOCO

        # Movimenta o retângulo para a nova posição
        self.canvas.coords(self.minhoca, self.x, self.y, self.x + TAMANHO_BLOCO, self.y + TAMANHO_BLOCO)

        # Verificar colisão com as bordas do campo
        if self.x < 0 or self.x >= LARGURA_CAMPO or self.y < 0 or self.y >= ALTURA_CAMPO:
            self.game_over()
        else:
            # Chama a função novamente após um intervalo de tempo
            self.root.after(100, self.movimento)

    def capturar_tecla(self, event):
        # Captura a tecla pressionada e muda a direção se válido
        if event.keysym == "w" or event.keysym == "Up":
            if self.direcao != BAIXO:
                self.direcao = CIMA
        elif event.keysym == "a" or event.keysym == "Left":
            if self.direcao != DIREITA:
                self.direcao = ESQUERDA
        elif event.keysym == "s" or event.keysym == "Down":
            if self.direcao != CIMA:
                self.direcao = BAIXO
        elif event.keysym == "d" or event.keysym == "Right":
            if self.direcao != ESQUERDA:
                self.direcao = DIREITA

    def game_over(self):
        # Exibe mensagem de fim de jogo e pergunta se o usuário quer jogar novamente
        self.canvas.create_text(LARGURA_CAMPO / 2, ALTURA_CAMPO / 2, text="Game Over!", fill="red", font=("Arial", 24))
        self.root.unbind("<KeyPress>")  # Desativa os controles temporariamente
        
        # Pergunta ao jogador se deseja jogar novamente
        resposta = messagebox.askyesno("Jogo da Minhoca", "Você perdeu! Deseja jogar novamente?")
        if resposta:
            self.reiniciar_jogo()
        else:
            self.root.quit()

    def reiniciar_jogo(self):
        # Reinicia as variáveis e a posição da minhoca
        self.x = LARGURA_CAMPO // 2
        self.y = ALTURA_CAMPO // 2
        self.direcao = DIREITA
        self.canvas.delete("all")  # Limpa o canvas
        self.minhoca = self.canvas.create_rectangle(self.x, self.y, self.x + TAMANHO_BLOCO, self.y + TAMANHO_BLOCO, fill="green")
        self.root.bind("<KeyPress>", self.capturar_tecla)  # Reativa os controles
        self.movimento()  # Reinicia o loop de movimentação

# Cria a janela e inicia o jogo
root = tk.Tk()
jogo = JogoMinhoca(root)
root.mainloop()
