import tkinter as tk
from tkinter import ttk

# === Configuração da janela principal ===
root = tk.Tk()
root.title("Login")
root.geometry("500x450")
root.configure(bg="#f2f2f2")
root.eval('tk::PlaceWindow . center')

# === Ícone (simulado com emoji 💙 + sinal de +) ===
canvas = tk.Canvas(root, width=100, height=80, bg="#f2f2f2", highlightthickness=0)
canvas.pack(pady=(30, 10))
canvas.create_text(25, 25, text="+", font=("Arial", 28, "bold"), fill="#2583f7")
canvas.create_text(65, 40, text="💙", font=("Arial", 40))

# === Título LOGIN ===
titulo = tk.Label(root, text="LOGIN", font=("Arial Black", 28, "italic"), bg="#f2f2f2", fg="black")
titulo.pack(pady=(0, 20))

# === FRAME dos campos ===
frame_campos = tk.Frame(root, bg="#f2f2f2")
frame_campos.pack()

# === Estilo dos campos ===
style = ttk.Style()
style.configure("Rounded.TEntry",
                padding=10,
                relief="flat",
                foreground="white",
                fieldbackground="#6da9e4",
                font=("Arial", 13))
style.map("Rounded.TEntry",
          focus=[("focus", {"fieldbackground": "#77b5f5"})])

# Campo Email
label_email = tk.Label(frame_campos, text="Email:", font=("Arial", 14), bg="#f2f2f2")
label_email.grid(row=0, column=0, sticky="e", padx=10, pady=10)
email_entry = ttk.Entry(frame_campos, style="Rounded.TEntry", width=22)
email_entry.grid(row=0, column=1, pady=10)
email_entry.insert(0, "Nome")

# Campo Senha
label_senha = tk.Label(frame_campos, text="Senha:", font=("Arial", 14), bg="#f2f2f2")
label_senha.grid(row=1, column=0, sticky="e", padx=10, pady=10)
senha_entry = ttk.Entry(frame_campos, style="Rounded.TEntry", width=22, show="*")
senha_entry.grid(row=1, column=1, pady=10)
senha_entry.insert(0, "Senha")

# === Botão ENTRAR ===
def entrar():
    print("Login realizado!")

botao = tk.Button(root,
                  text="ENTRAR",
                  font=("Arial Black", 12),
                  bg="#6da9e4",
                  fg="white",
                  activebackground="#5b98db",
                  activeforeground="white",
                  bd=0,
                  relief="flat",
                  cursor="hand2",
                  width=12,
                  height=1)
botao.pack(pady=(10, 10))

# Arredondamento simulado (borda circular)
botao.configure(highlightthickness=0)

# === Links de cadastro ===
link_frame = tk.Frame(root, bg="#f2f2f2")
link_frame.pack(pady=10)

texto1 = tk.Label(link_frame, text="Não possui cadastro?", font=("Arial", 11), bg="#f2f2f2", fg="blue")
texto1.pack()

def cadastrar():
    print("Abrir tela de cadastro...")

texto2 = tk.Label(link_frame, text="CADASTRAR-SE", font=("Arial", 10, "underline"), bg="#f2f2f2", fg="blue", cursor="hand2")
texto2.pack()
texto2.bind("<Button-1>", lambda e: cadastrar())

root.mainloop()