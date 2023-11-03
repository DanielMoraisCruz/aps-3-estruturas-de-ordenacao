from funcs_teste import print_colorido


def linha(msg, ajuste=0, tipo='-') -> str:
    if len(msg)-3 + ajuste % 2 == 0:
        larg = (len(msg)-3 + ajuste) / 2
    else:
        larg = (len(msg)-2 + ajuste) // 2
    return f"|{tipo*larg}|{tipo*larg}|"


class Mensagem_terminal():
    def __init__(self) -> None:
        self.mensagem: list = []
        self.mensagem_colorida: list = []

    def add_mensagem(self, txt, cor=None, posicao=None) -> None:
        if posicao:
            self.mensagem.insert(posicao, f"{print_colorido(txt)}")
            self.mensagem_colorida.insert(posicao, f"{print_colorido(txt)}")
        else:
            self.mensagem.append(f"{print_colorido(txt)}\n")
            self.mensagem_colorida.append(f"{print_colorido(txt, cor)}\n")

    def add_linha(self, msg: str, tipo_='-') -> None:
        self.mensagem.append(linha(msg, tipo=tipo_) + "\n")
        self.mensagem_colorida.append(linha(msg, tipo=tipo_) + "\n")

    def retornar_mensagem(self):
        self.mensagem_str = ''
        for i in self.mensagem:
            self.mensagem_str += i

        return self.mensagem_str

    def retornar_mensagem_colorida(self):
        mensagem = ''
        for i in self.mensagem_colorida:
            mensagem += i
        return mensagem

    def remover_linha(self, indice: int) -> None:
        self.mensagem.pop(indice)
        self.mensagem_colorida.pop(indice)
