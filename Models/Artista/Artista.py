class Artista:
    def __init__(self, nome):
        self.__nome = nome
        self.__saldo = 0.0
        self._streams_validos = 0
        self._ouvintes_unicos = 0
        self._retencao_por_conteudo = {}

    @property
    def nome(self):
        return self.__nome

    @property
    def saldo(self):
        return self.__saldo

    def _adicionar_receita(self, valor):
        self.__saldo += valor

    def registrar_stream(self, conteudo_id, retencao):
        self._streams_validos += 1
        self._retencao_por_conteudo.setdefault(conteudo_id, [])
        self._retencao_por_conteudo[conteudo_id].append(retencao)

    def relatorio_desempenho(self):
        print(f"Relatório do artista {self.__nome}")
        print(f"Streams válidos: {self._streams_validos}")
        print(f"Ouvintes únicos: {self._ouvintes_unicos}")
        print("Retenção média por conteúdo:")
        for conteudoid, retencao_lista in self._retencao_por_conteudo.items():
            media_retencao = sum(retencao_lista) / len(retencao_lista)
            print(f" - {conteudoid}: {media_retencao:.2f}%")
