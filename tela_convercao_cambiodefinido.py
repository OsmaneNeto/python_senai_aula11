import tkinter as biblioteca
#conda install -c anaconda tk
def converMoeda():
    moeda = entry.get()# get pega a entrada do texto #entry seu input# input -> get
    moeda = (float(moeda))
    taxaC = entradaTaxa.get()
    taxaC = (float(taxaC))
    conversao = taxaC*moeda
    labelres["text"] = conversao

window = biblioteca.Tk()

window.title("Curso de python")#titulo da interface

label = biblioteca.Label(window, text="Digite o valor da moeda: ")#rotulo
label.pack()#Entreada do rotulo definido

entry = biblioteca.Entry(window)#campo de entrada de dados
entry.pack()#chmada ao campo de texto



labelTaxa = biblioteca.Label(window, text="Digite o valor da taxa de cambio: ")#rotulo
labelTaxa.pack()#Entreada do rotulo definido

entradaTaxa = biblioteca.Entry(window)#campo de entrada de dados
entradaTaxa.pack()#chmada ao campo de texto

labelSaida = biblioteca.Label(window, text="Esse é o valor da conversão: ")#rotulo
labelSaida.pack()

labelres = biblioteca.Label(window, text="")#Rotulo
labelres.pack()#Chama ao rotulo definido

button = biblioteca.Button(window, text="mostrar", command=converMoeda)
button.pack()

window.geometry("300x200")
window.mainloop()#mainloop é um método para que o programa rode constantemente, caso contrario o programa ira rodar por um milesimo e irá encerrar.