import tkinter as tk
from tkinter import ttk

# === Configuração da janela principal ===
root = tk.Tk()
root.title("Cadastro")
root.geometry("500x500")
root.configure(bg="#f2f2f2")
root.eval('tk::PlaceWindow . center')

# === Ícone (sinal de + e coração azul) ===
canvas = tk.Canvas(root, width=100, height=80, bg="#f2f2f2", highlightthickness=0)
canvas.pack(pady=(30, 10))
canvas.create_text(25, 25, text="+", font=("Arial", 28, "bold"), fill="#2583f7")
canvas.create_text(65, 40, text="💙", font=("Arial", 40))

# === Título CADASTRAR-SE ===
titulo = tk.Label(root, text="CADASTRAR-SE", font=("Arial Black", 24, "italic"), bg="#f2f2f2", fg="black")
titulo.pack(pady=(0, 20))

# === FRAME dos campos ===
frame_campos = tk.Frame(root, bg="#f2f2f2")
frame_campos.pack()

# === Estilo dos campos arredondados ===
style = ttk.Style()
style.configure("Rounded.TEntry",
                padding=10,
                relief="flat",
                foreground="white",
                fieldbackground="#6da9e4",
                font=("Arial", 13))
style.map("Rounded.TEntry",
          focus=[("focus", {"fieldbackground": "#77b5f5"})])

# Campo Nome
label_nome = tk.Label(frame_campos, text="Nome:", font=("Arial", 13), bg="#f2f2f2")
label_nome.grid(row=0, column=0, sticky="e", padx=10, pady=10)
nome_entry = ttk.Entry(frame_campos, style="Rounded.TEntry", width=22)
nome_entry.grid(row=0, column=1, pady=10)
nome_entry.insert(0, "Nome")

# Campo Senha
label_senha = tk.Label(frame_campos, text="Senha:", font=("Arial", 13), bg="#f2f2f2")
label_senha.grid(row=1, column=0, sticky="e", padx=10, pady=10)
senha_entry = ttk.Entry(frame_campos, style="Rounded.TEntry", width=22, show="*")
senha_entry.grid(row=1, column=1, pady=10)
senha_entry.insert(0, "Senha")

# Campo Email
label_email = tk.Label(frame_campos, text="Email:", font=("Arial", 13), bg="#f2f2f2")
label_email.grid(row=2, column=0, sticky="e", padx=10, pady=10)
email_entry = ttk.Entry(frame_campos, style="Rounded.TEntry", width=22)
email_entry.grid(row=2, column=1, pady=10)
email_entry.insert(0, "Email")

# === Botão CADASTRAR ===
def cadastrar():
    print("Cadastro realizado!")

botao = tk.Button(root,
                  text="Cadastrar",
                  font=("Arial", 12, "bold"),
                  bg="#1976d2",
                  fg="white",
                  activebackground="#1565c0",
                  activeforeground="white",
                  bd=0,
                  relief="flat",
                  cursor="hand2",
                  width=15,
                  height=1)
botao.pack(pady=(15, 10))

# === Texto “Conecte-se com suas redes sociais” ===
texto_social = tk.Label(root, 
                        text="conecte-se com suas\nredes sociais", 
                        font=("Arial", 10, "underline"), 
                        bg="#f2f2f2", 
                        fg="blue", 
                        cursor="hand2", 
                        justify="center")
texto_social.pack(pady=(5, 10))

# === Ícones de redes sociais (simulados com emojis) ===
frame_icons = tk.Frame(root, bg="#f2f2f2")
frame_icons.pack(pady=(5, 20))

google = tk.Label(frame_icons, text="🌐", font=("Arial", 22), bg="#f2f2f2", cursor="hand2")
facebook = tk.Label(frame_icons, text="📘", font=("Arial", 22), bg="#f2f2f2", cursor="hand2")
apple = tk.Label(frame_icons, text="🍎", font=("Arial", 22), bg="#f2f2f2", cursor="hand2")

google.grid(row=0, column=0, padx=10)
facebook.grid(row=0, column=1, padx=10)
apple.grid(row=0, column=2, padx=10)

root.mainloop()