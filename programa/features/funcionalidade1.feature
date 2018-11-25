# language: pt

  Funcionalidade: criar uma lista e adicionar um item na lista.
    Cenario de Fundo: valores dentro da lista
    Esquema do Cenario: : criar uma lista e adicionar um item
      Dado o valor <valores>
      Quando criar a lista e adicionar o valor
      Entao se o valor dentro da lista e igual a o dado na lista <itens>
        E o ultimo item e <last>
      Exemplos: valores dentro da lista
      | valores     | itens       | last   |
      | 5           | [5]         | 5      |
      | 5, 3        | [5, 3]      | 3      |
      | 10.0, 6.3   | [10.0, 6.3] | 6.3    |
      | "a", "b"    | ["a", "b"]  | "b"    |
      | 6, "a"      | [6, "a"]    | "a"    |
      | 6, 3.8      | [6, 3.8]    | 3.8    |
      | "a", 8.4    | ["a", 8.4]  | 8.4    |