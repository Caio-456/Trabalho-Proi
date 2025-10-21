import Assinante

class Familia(Assinante):
    def __init__(self):
        super().__init__(
            tipo = "Família",
            preco = 40.90,
            beneficio = "Máximo de 5 contas diferentes e controle parental",
            limitacao = "Todos os usuários devem morar no mesmo endereço"
        )