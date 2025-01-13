import tkinter as tk


def adicionar_aluno():
    nome = entry_aluno.get()
    alunos.append(nome)
    entry_aluno.delete(0, tk.END)



def exibir_alunos():
    resultado_text.delete(1.0, tk.END)
    for aluno in alunos:
        resultado_text.insert(tk.END, aluno + "\n")


alunos = []


window = tk.Tk()
window.title("Cadastro de Alunos")
window.geometry("300x300")


label_aluno = tk.Label(window, text="Nome do Aluno:")
label_aluno.pack()


entry_aluno = tk.Entry(window)
entry_aluno.pack()


button_adicionar = tk.Button(window, text="Adicionar", command=adicionar_aluno)
button_adicionar.pack()


button_exibir = tk.Button(window, text="Exibir Alunos", command=exibir_alunos)
button_exibir.pack()


resultado_text = tk.Text(window, height=10, width=30)
resultado_text.pack()


window.mainloop()