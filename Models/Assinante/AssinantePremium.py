import Assinante

class Premium(Assinante):
    def __init__(self):
        super().__init__(
            tipo = "Premium",
            preco = 23.90,
            beneficio = "Acesso ilimitado a todos os conteúdos em alta definição",
            limitacao = "Máximo de um usúario por conta"
        )