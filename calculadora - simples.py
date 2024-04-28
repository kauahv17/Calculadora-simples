import tkinter as tk

tela = tk.Tk()
tela.title("calculadora")
tela.config(bg="black")

simbolos_matematicos = ["+", "-", "×", "÷", "^"]
simbolos_matematicos_alg = ["+", "-", "*", "/", "**"]


def arredondar(num):
    round_num = str(num)
    round_num = f"{float(round_num):_}"
    if "." in round_num:
        i = round_num.find(".")
        if len(round_num[i + 1 :]) > 7:
            round_num = round_num[: i + 1 + 7]
        elif len(round_num[i + 1 :]) == 1 and round_num[i + 1] == "0":
            round_num = round_num[:i]
    round_num = round_num.replace(".", ",").replace("_", ".")
    return round_num


def verificar_numero(num_1, icone, num_2):
    global mensagem_n1, mensagem_n2, mensagem_simbles

    situacao = True

    if num_1 == "":
        mensagem_n1["text"] = "coloque o primeiro número"
        situacao = False
    else:
        mensagem_n1["text"] = ""
    if num_2 == "":
        mensagem_n2["text"] = "coloque o segundo número"
        situacao = False
    else:
        mensagem_n2["text"] = ""
    if icone == "":
        mensagem_simbles["text"] = "selecione uma equação"
        situacao = False
    else:
        mensagem_simbles["text"] = ""

    for cr in num_1:
        if cr.isnumeric():
            pass
        else:
            mensagem_n1["text"] = "por favor, digite um número"
            situacao = False

    for cr in num_2:
        if cr.isnumeric():
            pass
        else:
            mensagem_n2["text"] = "por favor, digite um número"
            situacao = False

    return situacao


def resolver():
    global num_1, icone, num_2
    global equacao, simbolos_matematicos, simbolos_matematicos_alg

    equacao["text"] = ""
    num_1 = N1.get()
    num_2 = N2.get()
    conta = f"{num_1}{icone}{num_2}"
    i = simbolos_matematicos_alg.index(icone)
    equacao["text"] = f"{num_1} {simbolos_matematicos[i]} {num_2}"
    situacao = verificar_numero(num_1, icone, num_2)
    if situacao:
        resultado = eval(conta)
        resultado = arredondar(resultado)
        exibir_resultado = tk.Label(
            text=f"""{"-"*70}resultado{"-"*70}\n
{resultado}""",
            font=("Arial", 16),
            height=3,
            width=8,
            bg="black",
            fg="green",
        )
        exibir_resultado.grid(
            row=5, column=1, rowspan=2, columnspan=3, pady=15, sticky="NSWE"
        )
    else:
        equacao["text"] = "ERRO"
        equacao["fg"] = "red"


def receber():
    global icone, equacao, num_1, num_2
    global simbolos_matematicos, simbolos_matematicos_alg

    icone = simbolo.get()
    i = simbolos_matematicos_alg.index(icone)
    equacao["text"] = f"{num_1} {simbolos_matematicos[i]} {num_2}"
    equacao["fg"] = "green"


simbolo = tk.StringVar(value="vazio")
num_1 = ""
icone = ""
num_2 = ""

labels_nums = [
    ("digite um número:", "orange", 1),
    ("digite outro número:", "yellow", 3),
]
for texto, front, coluna in labels_nums:
    tk.Label(text=texto, bg="black", fg=front, font=("Arial", 15)).grid(
        row=0, column=coluna, pady=15, sticky="NSWE"
    )

N1 = tk.Entry(tela, font=("Arial", 15), bg="orange", fg="black")
N1.grid(row=1, column=1, pady=15, sticky="NSWE")

N2 = tk.Entry(tela, font=("Arial", 15), bg="yellow", fg="black")
N2.grid(row=1, column=3, pady=15, sticky="NSWE")

botao_n2 = tk.Button(
    text="calcular", font=("Arial", 14), bg="green", fg="black", command=resolver
)
botao_n2.grid(row=2, column=2, pady=15, sticky="NSWE")

equacao = tk.Label(text="", font=("Arial", 19), bg="black", fg="green", width=8)
equacao.grid(row=1, column=2, pady=15, sticky="NSWE")

for i, simble in enumerate(simbolos_matematicos):
    simble_alg = simbolos_matematicos_alg[i]
    tk.Radiobutton(
        text=f"{simble}",
        font=("Arial", 18),
        height=2,
        width=4,
        bg="black",
        fg="red",
        variable=simbolo,
        value=simble_alg,
        command=receber,
    ).grid(row=3, column=i, sticky="NSWE")

mensagem_n1 = tk.Label(text="", bg="black", fg="orange", font=("Arial", 15))
mensagem_n1.grid(row=2, column=1, sticky="NSWE")

mensagem_n2 = tk.Label(text="", bg="black", fg="yellow", font=("Arial", 15))
mensagem_n2.grid(row=2, column=3, sticky="NSWE")

mensagem_simbles = tk.Label(text="", bg="black", fg="red", font=("Arial", 15))
mensagem_simbles.grid(row=4, column=0, columnspan=5, sticky="NSWE")

tela.mainloop()