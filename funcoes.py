
def acha_preco(url):
    import urllib.request

    pagina = urllib.request.urlopen(url)
    texto = pagina.read().decode("utf-8")
    inicio = texto.find(">$") + 2
    fim = texto.find("</", inicio)
    preco = texto[inicio:fim]

    return float(preco)


def consulta_preco():
    from time import sleep

    min = 4.70

    while True:
        comum = acha_preco("http://beans.itcarlow.ie/prices-loyalty.html")
        fidelidade = acha_preco("http://beans.itcarlow.ie/prices.html")


        menor_valor = (
            comum if comum <= fidelidade else fidelidade
        )

        pagina = (
            "cliente comum" if menor_valor == comum else "cliente fidelidade"
        )

    
        if comum >= min and fidelidade >= min:
            print("\nEspere...")
            print(f"\033[31mPreço Fidelidade: U${fidelidade:.2f}\033[m")
            print(f"\033[31mPreço Comum: U${comum:.2f}\033[m\n\033[m")
            sleep(4)

        else:
            print(f"\nCompre agora na pagina do {pagina}.")
            print(f"\033[32mPreço: U${menor_valor:.2f}\033[m\n")
            break

    return f"Preço ideal encontrado - Preço: U${menor_valor:.2f}"

def msg_whatsapp(msg):
    from pywhatkit import sendwhatmsg
    from datetime import datetime

    agora = datetime.now()
    hora = agora.hour
    minuto = agora.minute + 1

    sendwhatmsg("+5547984717831", msg, hora, minuto, 20, True, 10)
    print("\033[32mMensagem enviada no whatsapp\033[m")
    

