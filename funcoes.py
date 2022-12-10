
def identifica_preco(url):
    import urllib.request

    pagina = urllib.request.urlopen(url)
    texto = pagina.read().decode("utf-8")
    inicio = texto.find(">$") + 2
    fim = texto.find("</", inicio)
    preco = texto[inicio:fim]

    return float(preco)


def consulta_preco():
    from time import sleep

    valor_minino = 4.70

    while True:
        cliente_comum = identifica_preco("http://beans.itcarlow.ie/prices-loyalty.html")
        cliente_fidelidade = identifica_preco("http://beans.itcarlow.ie/prices.html")


        menor_valor = (
            cliente_comum if cliente_comum <= cliente_fidelidade else cliente_fidelidade
        )

        pagina = (
            "cliente comum" if menor_valor == cliente_comum else "cliente fidelidade"
        )

    
        if cliente_comum >= valor_minino and cliente_fidelidade >= valor_minino:
            print("\nEspere...")
            print(f"\033[31mPreço Fidelidade: U${cliente_fidelidade:.2f}\033[m")
            print(f"\033[31mPreço Comum: U${cliente_comum:.2f}\033[m\n\033[m")
            sleep(4)

        else:
            print(f"\nCompre agora na pagina do {pagina}.")
            print(f"\033[32mPreço: U${menor_valor:.2f}\033[m\n")
            break

    return f"Preço ideal encontrado - Preço: U${menor_valor:.2f}"

def msg_whatsapp(mensagem):
    from pywhatkit import sendwhatmsg
    from datetime import datetime

    agora = datetime.now()
    hora = agora.hour
    minuto = agora.minute + 1

    sendwhatmsg("+5547984717831", mensagem, hora, minuto, 20, True, 10)
    print("\033[32mMensagem enviada no whatsapp\033[m")
    

