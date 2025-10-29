import tkinter as tk
from tkinter import font

def criar_dashboard():
    # 1. Configuração da Janela Principal
    root = tk.Tk()
    root.title("Dashboard Consult+")
    
    # Definir um tamanho fixo (aproximado) e centralizar
    LARGURA = 1200
    ALTURA = 750
    root.geometry(f'{LARGURA}x{ALTURA}')
    root.resizable(False, False)
    root.configure(bg='#f0f0f0') # Cor de fundo cinza claro

    # --- Definições de Cores e Fontes ---
    COR_FUNDO_CINZA = '#f0f0f0'
    COR_BRANCO = '#ffffff'
    COR_TEXTO_PADRAO = '#4a4a4a'
    COR_AZUL_MARINHO = '#0f4c81'
    
    # Cores das Métricas e Gráficos
    CORES_METRICAS = {
        'agendados': '#6d6d6d',
        'confirmados': '#1e88e5',
        'atendidos': '#4caf50',
        'faltaram': '#e53935'
    }
    CORES_GRAFICO = {
        'recorrentes': '#03a9f4', # Azul claro
        'novos': '#01579b',       # Azul escuro
        'consulta': '#ff8a65',    # Laranja
        'retorno': '#ffb74d',     # Amarelo claro
        'realizada': '#ff6347',   # Laranja avermelhado
        'particular': '#4caf50',  # Verde
        'publica': '#2e7d32'      # Verde escuro
    }

    fonte_menu = font.Font(family='Helvetica', size=11)
    fonte_card_numero = font.Font(family='Helvetica', size=40, weight='normal')
    fonte_card_texto = font.Font(family='Helvetica', size=11)
    fonte_titulo_secao = font.Font(family='Helvetica', size=14, weight='bold')

    # 2. Área de Navegação (Menu Superior)
    menu_frame = tk.Frame(root, bg=COR_BRANCO, height=50)
    menu_frame.pack(fill='x', side='top')

    # Título Principal
    lbl_logo = tk.Label(menu_frame, text="Consult+", font=('Helvetica', 14, 'bold'), fg=COR_AZUL_MARINHO, bg=COR_BRANCO)
    lbl_logo.pack(side='left', padx=(20, 10))
    lbl_dropdown = tk.Label(menu_frame, text="v", font=('Helvetica', 10), fg=COR_AZUL_MARINHO, bg=COR_BRANCO)
    lbl_dropdown.pack(side='left', padx=(0, 30))

    # Opções do Menu
    opcoes_menu = ["Painel", "Agenda", "Pacientes ▼", "Gestão ▼", "Outros"]
    for opcao in opcoes_menu:
        # Se for um dropdown (com ▼), simulamos
        texto = opcao.replace(' ▼', '')
        btn = tk.Label(menu_frame, text=texto, font=fonte_menu, fg=COR_TEXTO_PADRAO, bg=COR_BRANCO, padx=15)
        btn.pack(side='left')

    # Ícone do Usuário (Placeholder)
    lbl_user_icon = tk.Label(menu_frame, text="👤", font=('Arial', 24), bg=COR_BRANCO)
    lbl_user_icon.pack(side='right', padx=20)

    # 3. Seção de Métricas (Cartões Principais)
    metrics_frame = tk.Frame(root, bg=COR_FUNDO_CINZA)
    metrics_frame.pack(pady=40, padx=50, fill='x')

    # Dados das métricas
    metricas = [
        ("6", "Pacientes Agendados", CORES_METRICAS['agendados']),
        ("4", "Pacientes Confirmados", CORES_METRICAS['confirmados']),
        ("2", "Pacientes Atendidos", CORES_METRICAS['atendidos']),
        ("1", "Pacientes que Faltaram", CORES_METRICAS['faltaram'])
    ]

    # Função para criar um cartão de métrica
    def criar_cartao_metrica(parent, numero, texto, cor_numero, coluna):
        card = tk.Frame(parent, bg=COR_BRANCO, relief='flat', bd=0, padx=10, pady=20)
        card.grid(row=0, column=coluna, padx=10, sticky='nsew')
        
        # Número
        lbl_numero = tk.Label(card, text=numero, font=fonte_card_numero, fg=cor_numero, bg=COR_BRANCO)
        lbl_numero.pack(pady=(0, 5))
        
        # Texto
        lbl_texto = tk.Label(card, text=texto, font=fonte_card_texto, fg=cor_numero, bg=COR_BRANCO)
        lbl_texto.pack()
        
        # Estrutura para o fundo do 'card' arredondado (Apenas visual)
        # Em Tkinter puro, o jeito mais fácil é usar um canvas ou ignorar o arredondamento

    # Criar os 4 cartões
    for i, (num, txt, cor) in enumerate(metricas):
        criar_cartao_metrica(metrics_frame, num, txt, cor, i)
        metrics_frame.grid_columnconfigure(i, weight=1) # Distribui o espaço

    # 4. Seção Inferior (Gráficos)
    graficos_frame = tk.Frame(root, bg=COR_FUNDO_CINZA)
    graficos_frame.pack(pady=20, padx=50, fill='both', expand=True)
    
    # --- GRÁFICO 1: Pacientes (Pizza e Mini-Donut) ---
    def criar_painel_pacientes(parent, coluna):
        painel = tk.Frame(parent, bg=COR_BRANCO, relief='flat', bd=1, padx=20, pady=15)
        painel.grid(row=0, column=coluna, padx=15, sticky='nsew')
        
        lbl_titulo = tk.Label(painel, text="Pacientes", font=fonte_titulo_secao, bg=COR_BRANCO, fg=COR_TEXTO_PADRAO)
        lbl_titulo.pack(pady=(0, 10), anchor='w')
        
        # Simulação do Gráfico de Pizza (Canvas)
        canvas_pizza = tk.Canvas(painel, width=150, height=150, bg=COR_BRANCO, highlightthickness=0)
        canvas_pizza.pack(pady=10)
        
        # Pizza (coordenadas: x0, y0, x1, y1)
        canvas_pizza.create_arc(10, 10, 140, 140, start=90, extent=135, fill=CORES_GRAFICO['recorrentes'], outline=COR_BRANCO, width=1) # 37.5%
        canvas_pizza.create_arc(10, 10, 140, 140, start=90+135, extent=225, fill=CORES_GRAFICO['novos'], outline=COR_BRANCO, width=1) # 62.5%
        
        # Legenda e Mini-Gráficos (Simplificados)
        legend_frame = tk.Frame(painel, bg=COR_BRANCO)
        legend_frame.pack(pady=10)
        
        # Recorrentes/Novos
        tk.Label(legend_frame, text="■ Recorrentes", fg=CORES_GRAFICO['recorrentes'], bg=COR_BRANCO, font=fonte_card_texto).pack(side='left', padx=5)
        tk.Label(legend_frame, text="■ Novos", fg=CORES_GRAFICO['novos'], bg=COR_BRANCO, font=fonte_card_texto).pack(side='left', padx=5)
        
        # Sexo (Mini-Donuts)
        mini_frame = tk.Frame(painel, bg=COR_BRANCO)
        mini_frame.pack(pady=5)
        
        tk.Label(mini_frame, text="Mulher", fg=CORES_GRAFICO['realizada'], bg=COR_BRANCO, font=fonte_card_texto).pack(side='left', padx=15)
        tk.Label(mini_frame, text="Homem", fg=CORES_GRAFICO['novos'], bg=COR_BRANCO, font=fonte_card_texto).pack(side='left', padx=15)

    # --- GRÁFICO 2: Procedimentos Realizados (Donut) ---
    def criar_painel_procedimentos(parent, coluna):
        painel = tk.Frame(parent, bg=COR_BRANCO, relief='flat', bd=1, padx=20, pady=15)
        painel.grid(row=0, column=coluna, padx=15, sticky='nsew')
        
        lbl_titulo = tk.Label(painel, text="Procedimentos Realizados", font=fonte_titulo_secao, bg=COR_BRANCO, fg=COR_TEXTO_PADRAO)
        lbl_titulo.pack(pady=(0, 10), anchor='w')
        
        # Simulação do Gráfico Donut (Canvas)
        canvas_donut = tk.Canvas(painel, width=150, height=150, bg=COR_BRANCO, highlightthickness=0)
        canvas_donut.pack(pady=10)
        
        # Donut (Arco maior e Círculo interno para simular o "buraco")
        canvas_donut.create_arc(10, 10, 140, 140, start=0, extent=120, fill=CORES_GRAFICO['consulta'], outline=COR_BRANCO, width=1)
        canvas_donut.create_arc(10, 10, 140, 140, start=120, extent=80, fill=CORES_GRAFICO['retorno'], outline=COR_BRANCO, width=1)
        canvas_donut.create_arc(10, 10, 140, 140, start=200, extent=160, fill=CORES_GRAFICO['realizada'], outline=COR_BRANCO, width=1)
        
        # Círculo central para o "buraco" do donut
        canvas_donut.create_oval(40, 40, 110, 110, fill=COR_BRANCO, outline=COR_BRANCO)
        
        # Legenda (Simples)
        legend_data = [
            ("Consulta", CORES_GRAFICO['consulta']),
            ("Retorno", CORES_GRAFICO['retorno']),
            ("Realizada", CORES_GRAFICO['realizada'])
        ]
        
        for i, (texto, cor) in enumerate(legend_data):
            tk.Label(painel, text=f"■ {texto}", fg=cor, bg=COR_BRANCO, font=fonte_card_texto).pack(anchor='w', padx=5, pady=2)


    # --- GRÁFICO 3: Tipo de Consulta (Barras) ---
    def criar_painel_tipo_consulta(parent, coluna):
        painel = tk.Frame(parent, bg=COR_BRANCO, relief='flat', bd=1, padx=20, pady=15)
        painel.grid(row=0, column=coluna, padx=15, sticky='nsew')
        
        lbl_titulo = tk.Label(painel, text="Tipo de Consulta", font=fonte_titulo_secao, bg=COR_BRANCO, fg=COR_TEXTO_PADRAO)
        lbl_titulo.pack(pady=(0, 10), anchor='w')
        
        # Simulação do Gráfico de Barras (Canvas)
        canvas_barras = tk.Canvas(painel, width=200, height=150, bg=COR_BRANCO, highlightthickness=0)
        canvas_barras.pack(pady=10)
        
        # Barras (coordenadas: x0, y0, x1, y1)
        # Particular (Menor)
        canvas_barras.create_rectangle(50, 50, 80, 140, fill=CORES_GRAFICO['particular'], outline=CORES_GRAFICO['particular'])
        # Pública (Maior)
        canvas_barras.create_rectangle(120, 20, 150, 140, fill=CORES_GRAFICO['publica'], outline=CORES_GRAFICO['publica'])
        
        # Eixo X
        canvas_barras.create_line(40, 140, 160, 140, fill='#cccccc')
        
        # Legenda
        legend_frame = tk.Frame(painel, bg=COR_BRANCO)
        legend_frame.pack(pady=10)
        tk.Label(legend_frame, text="■ Particular", fg=CORES_GRAFICO['particular'], bg=COR_BRANCO, font=fonte_card_texto).pack(side='left', padx=5)
        tk.Label(legend_frame, text="■ Pública", fg=CORES_GRAFICO['publica'], bg=COR_BRANCO, font=fonte_card_texto).pack(side='left', padx=5)

    # Configurar o layout dos gráficos
    graficos_frame.grid_columnconfigure(0, weight=1)
    graficos_frame.grid_columnconfigure(1, weight=1)
    graficos_frame.grid_columnconfigure(2, weight=1)
    
    criar_painel_pacientes(graficos_frame, 0)
    criar_painel_procedimentos(graficos_frame, 1)
    criar_painel_tipo_consulta(graficos_frame, 2)
    
    root.mainloop()

if __name__ == "__main__":
    criar_dashboard()