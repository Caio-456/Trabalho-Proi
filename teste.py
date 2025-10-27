import csv

class Musica:
    def __init__(self, titulo, artista, data, duracao, genero, isrc, album, faixa, selo, explicito):
        self.__titulo = titulo
        self.__artista = artista
        self.__data = data
        self.__duracao = duracao
        self.__genero = genero
        self.__isrc = isrc
        self.__album = album
        self.__faixa = faixa
        self.__selo = selo
        self.__explicito = explicito

    def __str__(self):
        return 'Deu certo!'


class Podcast:
    def __init__(self, titulo, artista, data, duracao, genero, season, episode, rss, isrc):
        self.__titulo = titulo
        self.__artista = artista
        self.__data = data
        self.__duracao = duracao
        self.__genero = genero
        self.__season = season
        self.__episode = episode
        self.__rss = rss
        self.__isrc = isrc

    def __str__(self):
        return 'Deu certo!'


class AudioLivro:
    def __init__(self, titulo, artista, data, duracao, genero, narrador, editora, capitulos):
        self.__titulo = titulo
        self.__artista = artista
        self.__data = data
        self.__duracao = duracao
        self.__genero = genero
        self.__narrador = narrador
        self.__editora = editora
        self.__capitulos = capitulos

    def __str__(self):
        return 'Deu certo!'


class SomAmbiente:
    def __init__(self, titulo, artista, data, duracao, genero, loopable, ruido):
        self.__titulo = titulo
        self.__artista = artista
        self.__data = data
        self.__duracao = duracao
        self.__genero = genero
        self.__loopable = loopable
        self.__ruido = ruido

    def __str__(self):
        return 'Deu certo!'

class ConteudoServices:
    def __init__(self):
        self.__musicas = []
        self.__podcasts = []
        self.__audiolivros = []
        self.__sons_ambiente = []
        self.erros = []

    def carregar_csv(self, nome_arquivo):
        with open(nome_arquivo, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")

            for i, row in enumerate(reader, start=1):
                tipo = row["content_type"].lower()

                try:
                    if tipo == "musica":
                        if not row["identifier/ISRC"]:
                            raise ValueError("Música sem ISRC não pode ser cadastrada")
                        musica = Musica(
                            row["title"], row["artist_id"], row["release_date"],
                            int(row["duration_sec"]), row["genre"],
                            row["identifier/ISRC"], row["album"],
                            row["Faixa"], row["selo"], row["explicit"]
                        )
                        self.musicas.append(musica)

                    elif tipo == "podcast":
                        if not row["rss_feed"]:
                            raise ValueError("Podcast sem RSS Feed")
                        podcast = Podcast(
                            row["title"], row["artist_id"], row["release_date"],
                            int(row["duration_sec"]), row["genre"],
                            row["season"], row["episode"],
                            row["rss_feed"], row["identifier/ISRC"]
                        )
                        self.podcasts.append(podcast)

                    elif tipo == "audiolivro":
                        if not row["narrator"] or not row["editora"]:
                            raise ValueError("Audiolivro sem narrador ou editora")
                        audiobook = AudioLivro(
                            row["title"], row["artist_id"], row["release_date"],
                            int(row["duration_sec"]), row["genre"],
                            row["narrator"], row["editora"], row["capítulo"]
                        )
                        self.audiolivros.append(audiobook)

                    elif tipo == "som_ambiente":
                        som = SomAmbiente(
                            row["title"], row["artist_id"], row["release_date"],
                            int(row["duration_sec"]), row["genre"],
                            row["is_loopable"], row["noise_level"]
                        )
                        self.sons_ambiente.append(som)

                    else:
                        raise ValueError(f"Tipo desconhecido: {tipo}")

                except ValueError as e:
                    self.erros.append({"linha": i, "erro": str(e), "conteudo": row})

service = ConteudoServices()
service.carregar_csv("lancamentos.csv")
print(service.musicas)
print(service.podcasts)
print(service.audiolivros)
print(service.sons_ambiente)
print(service.erros)