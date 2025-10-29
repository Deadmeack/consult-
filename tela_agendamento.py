import tkinter as tk
from tkinter import font

def criar_tela_agendamentos():
    # 1. Configuração da Janela Principal
    root = tk.Tk()
    root.title("Agendamentos - Ana Luísa")
    
    # Definir um tamanho fixo (aproximado)
    LARGURA = 900
    ALTURA = 650
    root.geometry(f'{LARGURA}x{ALTURA}')
    root.resizable(False, False)
    root.configure(bg='#ffffff') # Fundo branco

    # --- Definições de Cores e Fontes ---
    COR_BRANCO = '#ffffff'
    COR_FUNDO_SEPARADOR = '#f7f7f7' # Cinza claro para linhas
    COR_TEXTO_PADRAO = '#333333'
    COR_TEXTO_SEGUNDARIO = '#777777'
    COR_LINK = '#1e88e5' # Azul para o link "Alterar"

    # Fontes
    fonte_perfil = font.Font(family='Helvetica', size=24, weight='bold')
    fonte_endereco = font.Font(family='Helvetica', size=11)
    fonte_agenda_titulo = font.Font(family='Helvetica', size=12, weight='bold')
    fonte_agenda_corpo = font.Font(family='Helvetica', size=11)
    fonte_link = font.Font(family='Helvetica', size=11, underline=1)
    fonte_cabecalho_tabela = font.Font(family='Helvetica', size=10, weight='bold')
    fonte_dados_tabela = font.Font(family='Helvetica', size=11)
    
    # 2. Botão Voltar
    btn_voltar = tk.Button(root, text="←", font=('Arial', 24, 'bold'), 
                           bg=COR_BRANCO, fg=COR_TEXTO_PADRAO, 
                           bd=0, relief='flat', activebackground='#eeeeee')
    btn_voltar.place(x=20, y=20)
    
    # 3. Informações de Perfil
    perfil_frame = tk.Frame(root, bg=COR_BRANCO)
    perfil_frame.place(x=80, y=50)

    # 3.1. Foto de Perfil (Simulada com Canvas)
    canvas_foto = tk.Canvas(perfil_frame, width=80, height=80, bg=COR_BRANCO, highlightthickness=0)
    canvas_foto.pack(side='left', padx=15, pady=5)
    # Simula o círculo da foto de perfil
    canvas_foto.create_oval(0, 0, 80, 80, fill='#cccccc', outline=COR_BRANCO)
    # Ícone placeholder (Simulando uma imagem)
    canvas_foto.create_text(40, 40, text="👤", font=('Arial', 40), fill=COR_TEXTO_PADRAO) 
    
    # 3.2. Nome e Endereço
    info_frame = tk.Frame(perfil_frame, bg=COR_BRANCO)
    info_frame.pack(side='left', anchor='n')

    lbl_nome = tk.Label(info_frame, text="Ana Luísa da Silva", font=fonte_perfil, fg=COR_TEXTO_PADRAO, bg=COR_BRANCO, anchor='w')
    lbl_nome.pack(fill='x', pady=(0, 0))
    
    lbl_endereco = tk.Label(info_frame, text="Rua: A Jardim Maravilha - Centro - Rio de Janeiro-RJ", font=fonte_endereco, fg=COR_TEXTO_SEGUNDARIO, bg=COR_BRANCO, anchor='w')
    lbl_endereco.pack(fill='x')
    
    # 4. Separador
    separator_frame = tk.Frame(root, height=1, bg='#e0e0e0')
    separator_frame.place(x=20, y=180, width=LARGURA - 40)
    
    # 5. Seção de Agendamento (Informações e Instrução)
    agenda_info_frame = tk.Frame(root, bg=COR_BRANCO)
    agenda_info_frame.place(x=80, y=200)

    # Agenda: Ana Luísa (Alterar)
    lbl_agenda_titulo = tk.Label(agenda_info_frame, text="Agenda: ", font=fonte_agenda_corpo, fg=COR_TEXTO_PADRAO, bg=COR_BRANCO)
    lbl_agenda_titulo.pack(side='left')
    lbl_agenda_nome = tk.Label(agenda_info_frame, text="Ana Luísa ", font=fonte_agenda_titulo, fg=COR_TEXTO_PADRAO, bg=COR_BRANCO)
    lbl_agenda_nome.pack(side='left')
    lbl_alterar = tk.Label(agenda_info_frame, text="(Alterar)", font=fonte_link, fg=COR_LINK, bg=COR_BRANCO, cursor="hand2")
    lbl_alterar.pack(side='left')
    
    # Instrução
    lbl_instrucao = tk.Label(root, text="Selecione o horário desejado na lista abaixo.", font=fonte_agenda_corpo, fg=COR_TEXTO_PADRAO, bg=COR_BRANCO)
    lbl_instrucao.place(x=80, y=240)
    
    # 6. Tabela de Agendamentos (Usando Grid para alinhamento)
    tabela_frame = tk.Frame(root, bg=COR_BRANCO)
    tabela_frame.place(x=80, y=290, width=LARGURA - 160)
    
    # Cabeçalhos da Tabela
    cabecalhos = ["Data:", "Horário Disponíveis:", "Tipo de consulta:", "Doutor(a):"]
    larguras_colunas = [0.2, 0.3, 0.25, 0.25]
    
    for i, texto in enumerate(cabecalhos):
        lbl_cabecalho = tk.Label(tabela_frame, text=texto, font=fonte_cabecalho_tabela, fg=COR_TEXTO_PADRAO, bg=COR_BRANCO, anchor='w')
        # Usamos place em um frame com grid para simular a distribuição de largura
        lbl_cabecalho.grid(row=0, column=i, sticky='w', padx=5, pady=5)
        tabela_frame.grid_columnconfigure(i, weight=1)

    # Dados da Tabela
    dados_agendamento = [
        ("13/04", "07:30 / 08:30", "Ginecologista", "Laura Lima", "📅", "🕒", "👩‍⚕️", "🧑‍⚕️"),
        ("12/05", "08:30 / 10:00", "Cardiologia", "Carlos Antônio", "📅", "🕒", "❤️", "🧑‍⚕️"),
        ("17/06", "08:30 / 10:00", "Cardiologia", "Carlos Antônio", "📅", "🕒", "❤️", "🧑‍⚕️"),
        ("10/07", "09:30 / 10:30", "Cardiologia", "Davi Souza", "📅", "🕒", "❤️", "🧑‍⚕️")
    ]
    
    def criar_linha_tabela(parent, dados, linha_index):
        # Frame para a linha
        row_frame = tk.Frame(parent, bg=COR_BRANCO)
        row_frame.grid(row=linha_index, column=0, columnspan=len(cabecalhos), sticky='ew')
        
        # Colunas
        for i, texto in enumerate(dados[:4]):
            icone = dados[4+i]
            
            # Frame interno para agrupar Ícone e Texto
            col_frame = tk.Frame(row_frame, bg=COR_BRANCO)
            col_frame.grid(row=0, column=i, sticky='w', padx=5, pady=10)
            row_frame.grid_columnconfigure(i, weight=1)

            # Ícone
            lbl_icone = tk.Label(col_frame, text=icone, font=('Arial', 14), fg=COR_TEXTO_SEGUNDARIO, bg=COR_BRANCO)
            lbl_icone.pack(side='left', padx=(0, 5))
            
            # Texto do dado
            lbl_dado = tk.Label(col_frame, text=texto, font=fonte_dados_tabela, fg=COR_TEXTO_PADRAO, bg=COR_BRANCO)
            lbl_dado.pack(side='left', anchor='w')

        # Separador horizontal abaixo da linha
        separator = tk.Frame(parent, height=1, bg='#eeeeee')
        separator.grid(row=linha_index + 1, column=0, columnspan=len(cabecalhos), sticky='ew')


    for i, dados in enumerate(dados_agendamento):
        criar_linha_tabela(tabela_frame, dados, i * 2 + 1) # Linhas ímpares para dados, pares para separador
        
    root.mainloop()

if __name__ == "__main__":
    criar_tela_agendamentos()