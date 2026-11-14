import tkinter as tk

segundos = 0
rodando = False

def atualizar():
    global segundos
    if rodando:
        segundos += 1
        horas = segundos // 3600
        minutos = (segundos % 3600) // 60
        seg = segundos % 60

        label.config(text=f"{horas:02}:{minutos:02}:{seg:02}")
        janela.after(1000, atualizar)

def iniciar():
    global rodando
    if not rodando:
        rodando = True
        atualizar()

def parar():
    global rodando
    rodando = False

def zerar():
    global segundos, rodando
    rodando = False
    segundos = 0
    label.config(text="00:00:00")

janela = tk.Tk()
janela.title("Cronômetro")
janela.geometry("300x200")

label = tk.Label(
    janela,
    text="00:00:00",
    font=("Arial", 24)
)
label.pack(pady=20)

tk.Button(janela, text="Iniciar", command=iniciar).pack()
tk.Button(janela, text="Parar", command=parar).pack()
tk.Button(janela, text="Zerar", command=zerar).pack()

janela.mainloop()