import tkinter as tk
from tkinter import font

def criar_tela_navegacao():
    # 1. Configuração da Janela Principal
    root = tk.Tk()
    root.title("Consult+ - Navegação")
    
    # Definir um tamanho fixo (aproximado)
    LARGURA = 800
    ALTURA = 550
    root.geometry(f'{LARGURA}x{ALTURA}')
    root.resizable(False, False)

    # --- Definições de Cores e Fontes ---
    COR_FUNDO_PRINCIPAL = '#576f7c' # Azul-cinzento escuro
    COR_BORDA_BRANCA = '#e0e0e0'    # Borda fina clara
    COR_BOTAO_FUNDO = '#e9e6e4'      # Fundo bege/rosado claro
    COR_TEXTO_PADRAO = '#2c3e50'    # Texto escuro
    COR_ICONE_CORACAO = '#b0e0e6'   # Azul claro (Coração)
    
    # Configurar o fundo da janela
    root.configure(bg=COR_FUNDO_PRINCIPAL)

    # Fontes
    fonte_titulo = font.Font(family='Times New Roman', size=52, weight='normal')
    fonte_botao = font.Font(family='Helvetica', size=14, weight='bold')

    # 2. Borda Externa (Canvas para desenhar o retângulo)
    canvas_borda = tk.Canvas(root, width=LARGURA - 40, height=ALTURA - 40, 
                             bg=COR_FUNDO_PRINCIPAL, highlightthickness=1, highlightbackground=COR_BORDA_BRANCA)
    canvas_borda.place(x=20, y=20)

    # 3. Cabeçalho
    
    # Título Principal
    lbl_titulo = tk.Label(root, text="Consult", font=fonte_titulo, fg=COR_TEXTO_PADRAO, bg=COR_FUNDO_PRINCIPAL)
    lbl_titulo.place(relx=0.5, rely=0.2, anchor='e') # Coloca a primeira parte à esquerda do centro
    
    # Símbolo "+"
    lbl_plus = tk.Label(root, text="+", font=('Times New Roman', 32, 'normal'), fg=COR_TEXTO_PADRAO, bg=COR_FUNDO_PRINCIPAL)
    lbl_plus.place(relx=0.5, rely=0.19, anchor='w') # Posiciona após o título

    # Ícone do Coração (Placeholder com caractere Unicode)
    lbl_coracao = tk.Label(root, text="💙", font=('Arial', 32), fg=COR_ICONE_CORACAO, bg=COR_FUNDO_PRINCIPAL)
    lbl_coracao.place(relx=0.5, rely=0.2, anchor='w', x=30) # Posiciona após o "+"

    # Ícone do Usuário (Placeholder com caractere Unicode em um círculo)
    # Usaremos um Canvas para o círculo e um Label para o ícone
    canvas_user = tk.Canvas(root, width=50, height=50, bg=COR_FUNDO_PRINCIPAL, highlightthickness=0)
    canvas_user.create_oval(0, 0, 50, 50, fill='#ffe0b2', outline='#f0e68c') # Simula o círculo da foto
    canvas_user.place(relx=0.9, rely=0.15, anchor='center')
    lbl_user = tk.Label(root, text="👤", font=('Arial', 24), bg='#ffe0b2') # Ícone sobre a cor da pele
    lbl_user.place(relx=0.9, rely=0.15, anchor='center')
    
    # 4. Botões de Ação (Grid 2x2 simulado com place)
    
    # Dimensões e Posições
    LARGURA_BOTAO = 300
    ALTURA_BOTAO = 70
    CENTRO_X = LARGURA // 2
    CENTRO_Y = ALTURA // 2
    ESPACAMENTO = 50
    
    # Posições Calculadas para o Grid
    x1 = CENTRO_X - LARGURA_BOTAO // 2 - ESPACAMENTO // 2 # Esquerda
    x2 = CENTRO_X + LARGURA_BOTAO // 2 + ESPACAMENTO // 2 # Direita
    y1 = CENTRO_Y                                        # Linha 1
    y2 = CENTRO_Y + ALTURA_BOTAO + ESPACAMENTO           # Linha 2
    
    # Função para criar um botão personalizado com ícone
    def criar_botao_acao(texto, icone_char, x_pos, y_pos):
        # Frame que simula o botão com fundo diferenciado
        btn_frame = tk.Frame(root, width=LARGURA_BOTAO, height=ALTURA_BOTAO, bg=COR_BOTAO_FUNDO, 
                             relief='flat', bd=0)
        btn_frame.pack_propagate(False) # Impedir que o frame se ajuste ao conteúdo
        
        # Cria um Label para o ícone (à esquerda)
        lbl_icone = tk.Label(btn_frame, text=icone_char, font=('Arial', 32), fg=COR_TEXTO_PADRAO, bg=COR_BOTAO_FUNDO)
        lbl_icone.pack(side='left', padx=15)
        
        # Cria um Label para o texto (centralizado)
        lbl_texto = tk.Label(btn_frame, text=texto, font=fonte_botao, fg=COR_TEXTO_PADRAO, bg=COR_BOTAO_FUNDO)
        lbl_texto.pack(side='left', padx=5)

        # Usamos Place para posicionar o frame que contém o botão/ícone
        btn_frame.place(x=x_pos, y=y_pos, anchor='center')
        
        # Adicionar funcionalidade (opcional)
        btn_frame.bind("<Button-1>", lambda e: print(f"Ação: {texto}"))
        for widget in btn_frame.winfo_children():
            widget.bind("<Button-1>", lambda e: print(f"Ação: {texto}"))

    # Ícones Placeholder (caracteres Unicode)
    ICON_AGENDAR = "📅✅"
    ICON_CANCELAR = "ⓧ"
    ICON_REAGENDAR = "📅🔄"
    ICON_MINHA_AGENDA = "🗓️"

    # 4.1. Agendar Consulta
    criar_botao_acao("Agendar Consulta", ICON_AGENDAR, CENTRO_X - (LARGURA_BOTAO/2 + 20), y1)

    # 4.2. Cancelar Consulta
    criar_botao_acao("Cancelar Consulta", ICON_CANCELAR, CENTRO_X + (LARGURA_BOTAO/2 + 20), y1)
    
    # 4.3. Reagendar Consulta
    criar_botao_acao("Reagendar Consulta", ICON_REAGENDAR, CENTRO_X - (LARGURA_BOTAO/2 + 20), y2)

    # 4.4. Minha Agenda
    criar_botao_acao("Minha Agenda", ICON_MINHA_AGENDA, CENTRO_X + (LARGURA_BOTAO/2 + 20), y2)

    root.mainloop()

if __name__ == "__main__":
    criar_tela_navegacao()