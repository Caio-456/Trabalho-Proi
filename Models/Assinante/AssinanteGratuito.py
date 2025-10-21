import Assinante

class Gratuito(Assinante):
    def __init__(self):
        super().__init__(
            tipo = "Gratuito",
            preco = 0.00,
            beneficio = "Acesso ao conteúdo básico",
            limitacao = "Sem downloads e anúncios periodicamente"
        )