from No import No


class Lista(No):
    def __init__(self):
        self.inicial = None
        self.final = None
        self._tamanho = 0

    @property
    def tamanho(self):
        return self._tamanho

    def append(self, valor):
        if self.inicial is None:
            self.inicial = self.final = No(valor)
        else:
            self.final.proximo = No(valor)
            self.final = self.final.proximo
        self._tamanho += 1
    @property
    def ultimo_item(self):
        return self.final.dado

    def mostra(self):
        iterador = self.inicial
        while iterador is not None:
            print(iterador)
            iterador = iterador.proximo

    def imprime(self):
        arq = open("teste.txt", "w")
        iterador = self.inicial
        while iterador is not None:
            arq.write(str(iterador))
            arq.write("\n")
            iterador = iterador.proximo

    def list_simple(self):
        itens = "["
        iterador = self.inicial
        while iterador is not None:
            itens += iterador.strsimple
            if iterador.proximo is not None:
                itens += ", "
            iterador = iterador.proximo
        itens += "]"
        return itens


