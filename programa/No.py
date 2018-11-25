class No:
    def __init__(self, valor):
        self._dado = valor
        self.proximo = None
        self.anterior = None

    def __str__(self):
        if self.proximo is None and self.anterior is None:
            return f"Anterior: {self.anterior} \t|\t Nó: {self.dado} \t|\t Próximo: {self.proximo}"
        elif self.proximo is None and self.anterior is not None:
            return f"Anterior: {self.anterior.dado} \t|\t Nó: {self.dado} \t|\t Próximo: {self.proximo}"
        elif self.anterior is None and self.proximo is not None:
            return f"Anterior: {self.anterior} \t|\t Nó: {self.dado} \t|\t Próximo: {self.proximo.dado}"
        else:
            return f"Anterior: {self.anterior.dado} \t|\t Nó: {self.dado} \t|\t Próximo: {self.proximo.dado}"

    @property
    def dado(self):
        return self._dado


    @property
    def strsimple(self):
        return str(self.dado)

