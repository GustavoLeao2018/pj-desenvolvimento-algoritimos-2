class No:
    def __init__(self, valor):
        self.dado = valor
        self.proximo = None

    def __str__(self):
        if self.proximo is None:
            return f"Nó: {self.dado} \t|\t Próximo: {self.proximo}"
        else:
            return f"Nó: {self.dado} \t|\t Próximo: {self.proximo.dado}"
