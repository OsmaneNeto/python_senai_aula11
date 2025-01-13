import tkinter as biblioteca
#taxaCambioD= 4.798
#taxaCambioE= 5.27



def converMoeda():
    moeda = entry.get()# get pega a entrada do texto #entry seu input# input -> get
    moeda = (float(moeda))
    taxa = taxacamb.get()
    if taxa == "euro":
        taxaE = 0.18709
    else:
        taxaE = 0.210
    #taxaC = (float(taxacamb))
    conversao = taxaE*moeda
    labelres["text"] = conversao


window = biblioteca.Tk()

window.title("Curso de python")#titulo da interface

label = biblioteca.Label(window, text="Digite o valor em Real brasileiro: ")#rotulo
label.pack()#Entreada do rotulo definido

entry = biblioteca.Entry(window)#campo de entrada de dados
entry.pack()#chmada ao campo de texto


lista =["euro","dolar"]
taxacamb= biblioteca.StringVar(window)
taxacamb.set(lista[0])
botao = biblioteca.OptionMenu(window, taxacamb, *lista)
botao.pack()





labelSaida = biblioteca.Label(window, text="Esse é o valor da conversão: ")#rotulo
labelSaida.pack()

labelres = biblioteca.Label(window, text="")#Rotulo
labelres.pack()#Chama ao rotulo definido

button = biblioteca.Button(window, text="mostrar", command=converMoeda)
button.pack()

window.geometry("300x200")
window.mainloop()#mainloop é um método para que o programa rode constantemente, caso contrario o programa ira rodar por um milesimo e irá encerrar.